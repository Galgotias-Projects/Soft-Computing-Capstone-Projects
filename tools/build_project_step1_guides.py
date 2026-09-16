from pathlib import Path
import ast

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tools" / "build_beginner_guide.py"
OUT = ROOT / "output" / "pdf" / "beginner-project-guides"
FONT_DIR = ROOT / "assets" / "fonts"
OUT.mkdir(parents=True, exist_ok=True)


def load_projects():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "PROJECTS" for target in node.targets):
                return ast.literal_eval(node.value)
    raise RuntimeError("PROJECTS data was not found")


PROJECTS = load_projects()

pdfmetrics.registerFont(TTFont("OpenSans", str(FONT_DIR / "OpenSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("OpenSans-SemiBold", str(FONT_DIR / "OpenSans-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("OpenSans-Bold", str(FONT_DIR / "OpenSans-Bold.ttf")))
pdfmetrics.registerFontFamily(
    "OpenSans",
    normal="OpenSans",
    bold="OpenSans-Bold",
    italic="OpenSans",
    boldItalic="OpenSans-Bold",
)

BLACK = colors.HexColor("#111111")
DARK = colors.HexColor("#333333")
MID = colors.HexColor("#666666")
LINE = colors.HexColor("#C8C8C8")
LIGHT = colors.HexColor("#EEEEEE")
PALE = colors.HexColor("#F7F7F7")
WHITE = colors.white


DETAILS = {
    "SC01": {
        "user": "A campus facility manager who wants a clear room-cooling recommendation.",
        "one_sentence": "Given room temperature, humidity, occupancy, and tariff, recommend cooling, fan level, and an energy action.",
        "fields": [
            ("scenario_id", "Unique row name", "text", "SC01-001, SC01-002, ..."),
            ("temperature_c", "Room temperature", "number in C", "18 to 45"),
            ("humidity_pct", "Relative humidity", "percentage", "20 to 100"),
            ("occupancy_count", "People in the room", "whole number", "0 to chosen room capacity"),
            ("tariff_level", "Current electricity price band", "category", "low, medium, high"),
        ],
        "samples": [
            ("SC01-001", "24, 50, 20, low", "Comfortable room; low cooling expected"),
            ("SC01-002", "36, 85, 45, medium", "Hot and humid; strong cooling/fan expected"),
            ("SC01-003", "38, 60, 0, high", "Empty room; energy-saving rule must apply"),
            ("SC01-004", "45, 70, 50, high", "Heat-wave boundary case"),
            ("SC01-005", "21, 90, 15, low", "Cool but humid; fan decision should be checked"),
        ],
        "baseline": [
            "If occupancy_count is 0, set cooling_pct to 0 and fan_level to off.",
            "Else if temperature_c is below 24, set cooling_pct to 10.",
            "Else if temperature_c is 24 to 30, set cooling_pct to 50.",
            "Else set cooling_pct to 90.",
            "If humidity_pct is above 75, increase fan_level by one band.",
            "If tariff_level is high, return energy_action as avoid_peak.",
        ],
        "screen": ("Temperature, humidity, occupancy, tariff", "Cooling %, fan level, energy action, baseline result, explanation"),
        "source_plan": "Find cited temperature/humidity ranges, room-capacity assumptions, and tariff bands. Later generate at least 10,000 valid combinations from those ranges.",
    },
    "SC02": {
        "user": "A washing-machine user who needs safe settings without wasting water or detergent.",
        "one_sentence": "Given dirt, load, fabric, and water availability, recommend wash time, water, detergent, and spin speed.",
        "fields": [
            ("scenario_id", "Unique wash-case name", "text", "SC02-001, SC02-002, ..."),
            ("dirt_score", "How dirty the clothes are", "number", "0 to 10"),
            ("load_kg", "Weight of clothes", "kg", "0.5 to chosen machine capacity"),
            ("fabric_type", "Main fabric", "category", "delicate, cotton, synthetic, heavy"),
            ("water_availability_pct", "Water available", "percentage", "0 to 100"),
        ],
        "samples": [
            ("SC02-001", "2, 3.0, cotton, 100", "Light dirt and half-load"),
            ("SC02-002", "9, 7.0, cotton, 100", "Heavy dirt and full load"),
            ("SC02-003", "5, 2.0, delicate, 80", "Delicate fabric must use safe spin"),
            ("SC02-004", "7, 5.0, synthetic, 25", "Low-water situation"),
            ("SC02-005", "6, 8.5, heavy, 70", "Over capacity; validation must reject"),
        ],
        "baseline": [
            "Create one fixed preset for delicate, cotton, synthetic, and heavy fabric.",
            "For each preset, write fixed wash_time_min, water_litre, detergent_ml, and spin_rpm.",
            "Ignore dirt and water availability in the baseline. That limitation is intentional.",
            "If load_kg is above machine capacity, do not return settings; show an error.",
        ],
        "screen": ("Dirt score, load kg, fabric, water availability", "Wash time, water, detergent, spin, baseline preset, warning"),
        "source_plan": "Choose one real machine capacity. Cite safe ranges or product documentation. Later generate at least 10,000 valid wash cases.",
    },
    "SC03": {
        "user": "A faculty mentor who wants early, supportive academic intervention information.",
        "one_sentence": "Given anonymous academic indicators, estimate a risk band and suggest a supportive intervention.",
        "fields": [
            ("record_id", "Anonymous row name", "text", "STU-001, STU-002, ..."),
            ("attendance_pct", "Classes attended", "percentage", "0 to 100"),
            ("assessment_pct", "Assessment marks", "percentage", "0 to 100"),
            ("assignment_pct", "Assignment marks", "percentage", "0 to 100"),
            ("engagement_score", "Participation indicator", "number", "0 to 10"),
            ("prior_performance_pct", "Earlier performance", "percentage", "0 to 100"),
            ("risk_label", "Expected label for testing", "category", "low, medium, high"),
        ],
        "samples": [
            ("STU-001", "92, 84, 88, 8, 81, low", "Consistently strong record"),
            ("STU-002", "42, 75, 78, 7, 74, medium", "Low attendance only"),
            ("STU-003", "55, 35, 30, 3, 40, high", "Several weak indicators"),
            ("STU-004", "78, 48, 52, 9, 45, medium", "High engagement but weak marks"),
            ("STU-005", "70, 60, 60, 5, 60, medium", "Boundary record"),
        ],
        "baseline": [
            "Calculate a visible score, for example 30% attendance + 30% assessment + 20% assignment + 10% engagement + 10% prior performance.",
            "Convert engagement_score to a percentage before using it.",
            "Use temporary bands: score below 50 high risk; 50 to 69 medium; 70 or more low.",
            "Map low to monitor, medium to mentoring/study plan, and high to faculty follow-up.",
            "State clearly that a human makes the final decision.",
        ],
        "screen": ("Anonymous academic indicators", "Risk band, score, intervention, baseline result, limitation note"),
        "source_plan": "Use only a public anonymized dataset. Record its URL, licence, columns, target, size, and privacy limitations. Do not collect names or phone numbers.",
    },
    "SC04": {
        "user": "A traffic operator studying one simple two-phase junction.",
        "one_sentence": "Given queues, density, waiting time, and emergency direction, choose the next phase and green duration.",
        "fields": [
            ("state_id", "Unique traffic state", "text", "TRF-001, TRF-002, ..."),
            ("queue_ns", "North-south queue", "vehicles", "0 or more"),
            ("queue_ew", "East-west queue", "vehicles", "0 or more"),
            ("density_ns_pct", "North-south density", "percentage", "0 to 100"),
            ("density_ew_pct", "East-west density", "percentage", "0 to 100"),
            ("max_wait_ns_sec", "Longest NS wait", "seconds", "0 to 300"),
            ("max_wait_ew_sec", "Longest EW wait", "seconds", "0 to 300"),
            ("emergency_direction", "Emergency approach", "category", "none, NS, EW"),
        ],
        "samples": [
            ("TRF-001", "5, 5, 20, 20, 25, 22, none", "Balanced low traffic"),
            ("TRF-002", "30, 6, 85, 25, 120, 30, none", "Heavy NS queue"),
            ("TRF-003", "4, 28, 15, 80, 20, 115, none", "Heavy EW queue"),
            ("TRF-004", "8, 12, 30, 40, 190, 65, none", "Long waiting time despite shorter NS queue"),
            ("TRF-005", "20, 20, 60, 60, 90, 90, EW", "Emergency must get priority"),
        ],
        "baseline": [
            "Start with NS green for 30 seconds.",
            "Then use EW green for 30 seconds.",
            "Continue alternating, even when one queue is longer.",
            "If emergency_direction is not none, allow an explicit safety override in the test version.",
            "Reject negative queues, density over 100, or wait above the selected limit.",
        ],
        "screen": ("NS/EW queue, density, wait, emergency", "Next phase, green seconds, baseline phase, queue chart, warning"),
        "source_plan": "Document arrival/departure assumptions and safe green-time limits. Later use a reproducible simulator to produce at least 10,000 states.",
    },
    "SC05": {
        "user": "A timetable coordinator who needs a clash-free weekly schedule.",
        "one_sentence": "Place courses into rooms and time slots without faculty, room, or cohort clashes.",
        "fields": [
            ("course_id", "Course name/code", "text", "C01 to C05"),
            ("cohort_id", "Student group", "text", "G1 or G2"),
            ("faculty_id", "Teacher", "text", "F1 to F3"),
            ("weekly_sessions", "Sessions required", "whole number", "1 to 4"),
            ("duration_slots", "Length of one session", "slots", "1 or 2"),
            ("required_room_type", "Room needed", "category", "classroom or lab"),
            ("room capacity/type", "Room properties", "number/category", "Must fit cohort and course"),
            ("slot day/time", "Available teaching time", "text/time", "10 clearly named slots"),
        ],
        "samples": [
            ("Fixture 1", "5 courses, 3 rooms, 10 slots", "A feasible timetable must exist"),
            ("Fixture 2", "Only one small room", "Room shortage must be reported"),
            ("Fixture 3", "Two courses, same faculty, same slot", "Faculty clash must be detected"),
            ("Fixture 4", "Two courses, same cohort, same slot", "Cohort clash must be detected"),
            ("Fixture 5", "Valid schedule outside preferred time", "Soft penalty, not hard failure"),
        ],
        "baseline": [
            "Read courses in file order.",
            "For each course, scan slots from first to last.",
            "Choose the first room and slot that does not create a hard clash.",
            "If no placement is possible, mark that course unplaced.",
            "Count unplaced courses and preference penalties.",
        ],
        "screen": ("Course, room, faculty, cohort, and slot tables", "Timetable grid, clash count, unplaced courses, penalty score"),
        "source_plan": "Create three small input files first. Later write a seeded generator that creates at least 10,000 timetable variations from documented rules.",
    },
    "SC06": {
        "user": "A campus shuttle or delivery planner choosing the visiting order for stops.",
        "one_sentence": "Given campus stops and distances, return a route that starts and ends at the depot.",
        "fields": [
            ("stop_id", "Short stop code", "text", "DEPOT, S01, S02, ..."),
            ("stop_name", "Readable place name", "text", "Library, Hostel, Lab, ..."),
            ("x_coordinate", "Simple map x position", "number", "One consistent map scale"),
            ("y_coordinate", "Simple map y position", "number", "One consistent map scale"),
            ("priority", "Visit importance", "category/number", "low, medium, high"),
            ("earliest_time", "Earliest allowed visit", "time", "HH:MM"),
            ("latest_time", "Latest allowed visit", "time", "HH:MM"),
        ],
        "samples": [
            ("Route 1", "Depot plus 6 normal stops", "Normal route should be calculated"),
            ("Route 2", "Two stops at the same distance", "Tie rule must be written"),
            ("Route 3", "One distant high-priority stop", "Priority effect must be visible"),
            ("Route 4", "One distance increased for traffic", "Route cost should change"),
            ("Route 5", "Impossible narrow time window", "Program must report infeasible"),
        ],
        "baseline": [
            "Start at DEPOT.",
            "Find the nearest stop that has not been visited.",
            "Move to that stop and add the distance to total_distance.",
            "Repeat until every stop is visited.",
            "Return to DEPOT and add the final distance.",
            "If two stops are equal, choose the alphabetically smaller stop_id.",
        ],
        "screen": ("Stop table and route options", "Visit order, route map, total distance/time, baseline result"),
        "source_plan": "Use cited coordinates/map distances or clearly simulated coordinates. Later create at least 10,000 traffic/route scenarios with a fixed random seed.",
    },
    "SC07": {
        "user": "A grower or farm manager deciding whether and how much to irrigate.",
        "one_sentence": "Given soil, weather, rainfall, and crop stage, recommend water and irrigation duration.",
        "fields": [
            ("scenario_id", "Unique irrigation case", "text", "IRR-001, IRR-002, ..."),
            ("soil_moisture_pct", "Water already in soil", "percentage", "0 to 100"),
            ("humidity_pct", "Air humidity", "percentage", "0 to 100"),
            ("temperature_c", "Air temperature", "C", "Use cited local range"),
            ("rainfall_mm", "Recent/forecast rain", "mm", "0 or more"),
            ("crop_stage", "Growth stage", "category", "initial, development, mid, late"),
        ],
        "samples": [
            ("IRR-001", "18, 30, 38, 0, mid", "Dry and hot; irrigation expected"),
            ("IRR-002", "62, 55, 28, 0, development", "Adequate moisture"),
            ("IRR-003", "35, 80, 25, 35, mid", "Recent heavy rain; likely off"),
            ("IRR-004", "20, 90, 30, 0, late", "Dry soil but high humidity"),
            ("IRR-005", "125, 45, 31, 0, initial", "Invalid sensor reading must be rejected"),
        ],
        "baseline": [
            "If rainfall_mm is at or above the chosen rain threshold, set irrigation off.",
            "Else if soil_moisture_pct is below the chosen moisture threshold, set irrigation on.",
            "Else set irrigation off.",
            "Use one fixed duration when on. This is deliberately simple.",
            "Reject moisture or humidity outside 0 to 100 and negative rainfall.",
        ],
        "screen": ("Soil moisture, humidity, temperature, rainfall, crop stage", "Water need, duration, decision, baseline result, warning"),
        "source_plan": "Choose one crop and area/flow assumption. Cite agriculture/weather data and units. Later prepare at least 10,000 records or documented scenarios.",
    },
    "SC08": {
        "user": "A maintenance engineer deciding which machine needs attention first.",
        "one_sentence": "Given machine sensor readings, estimate fault risk and maintenance priority.",
        "fields": [
            ("reading_id", "Unique sensor row", "text", "MCH-001, MCH-002, ..."),
            ("vibration", "Machine vibration", "dataset unit", "Use one cited dataset unit"),
            ("temperature_c", "Machine temperature", "C", "Use dataset range"),
            ("rpm", "Rotational speed", "revolutions/min", "0 or more"),
            ("load_pct", "Machine load", "percentage", "0 to 100"),
            ("severity", "Observed severity", "category/number", "Clearly defined"),
            ("fault_label", "Known result for testing", "category", "no_fault or chosen fault classes"),
        ],
        "samples": [
            ("MCH-001", "normal vibration/temp/rpm, 45%, low, no_fault", "Normal operation"),
            ("MCH-002", "high vibration only, 55%, medium, fault", "Single warning signal"),
            ("MCH-003", "high temperature and 95% load, high, fault", "Overheating under load"),
            ("MCH-004", "several extreme signals, high, fault", "Immediate priority expected"),
            ("MCH-005", "missing vibration, 70%, unknown, unknown", "Missing sensor must be handled"),
        ],
        "baseline": [
            "Write one temporary warning threshold for each sensor.",
            "Count how many thresholds are crossed.",
            "Zero crossed thresholds gives low risk; one gives medium; two or more gives high.",
            "Map low to routine, medium to soon, and high to immediate.",
            "Do not invent units. Copy units and ranges from one cited dataset.",
        ],
        "screen": ("Vibration, temperature, RPM, load, severity", "Fault risk, risk band, maintenance priority, baseline flags"),
        "source_plan": "Choose one public sensor dataset. Record machine type, sampling frequency, units, label meaning, class balance, and licence.",
    },
    "SC09": {
        "user": "An educational risk reviewer using an explainable decision-support prototype.",
        "one_sentence": "Given anonymous credit features, estimate risk, confidence, and a review recommendation.",
        "fields": [
            ("record_id", "Anonymous applicant row", "text", "CRD-001, CRD-002, ..."),
            ("income", "Income amount", "chosen currency", "Positive number"),
            ("loan_amount", "Requested loan", "same currency", "Positive number"),
            ("debt_to_income_pct", "Debt compared with income", "percentage", "0 or more; justify cap"),
            ("repayment_history", "Past repayment category", "category", "good, mixed, poor"),
            ("employment_length", "Time in employment", "years", "0 or more"),
            ("credit_target", "Dataset result", "category", "Define default/non-default clearly"),
        ],
        "samples": [
            ("CRD-001", "high income, low loan, 15, good, 8, low-risk target", "Stable case"),
            ("CRD-002", "medium income, high loan, 70, mixed, 3, high-risk target", "High debt"),
            ("CRD-003", "medium values near thresholds", "Borderline score"),
            ("CRD-004", "high income, poor history, 55, poor, 1, high-risk target", "Conflicting indicators"),
            ("CRD-005", "missing employment length", "Missing value must be handled"),
        ],
        "baseline": [
            "Start score at 0.",
            "Add risk points when debt_to_income_pct is high.",
            "Add risk points for mixed or poor repayment_history.",
            "Add risk points for very short employment_length.",
            "Use visible score bands for low, medium, and high risk.",
            "Keep risk prediction separate from recommended action. State that this is educational only.",
        ],
        "screen": ("Anonymous financial features", "Risk band, confidence, recommendation, baseline points, ethics note"),
        "source_plan": "Use only a public anonymized dataset. Record URL, licence, target distribution, sensitive features, encoding, and fairness plan.",
    },
    "SC10": {
        "user": "A home, lab, or small-building user planning appliance times and electricity use.",
        "one_sentence": "Given hourly load, tariff, and appliance limits, predict demand and choose a lower-cost schedule.",
        "fields": [
            ("date/hour", "Time of load record", "date and 0-23", "Exactly 24 rows for starter day"),
            ("historical_load_kw", "Earlier electricity demand", "kW", "0 or more"),
            ("temperature_c", "Weather input", "C", "Use cited range"),
            ("tariff_per_kwh", "Electricity price", "currency/kWh", "0 or more"),
            ("appliance_id", "Appliance name/code", "text", "APP-01, APP-02, ..."),
            ("power_kw", "Appliance power", "kW", "Positive number"),
            ("duration_slots", "Hours required", "whole number", "1 to 24"),
            ("earliest_start/latest_finish", "Allowed window", "hour", "0 to 23; start before finish"),
            ("interruptible/priority", "Scheduling rule", "boolean/category", "yes/no and low/medium/high"),
        ],
        "samples": [
            ("Case 1", "Flat tariff and normal appliances", "Baseline schedule should calculate"),
            ("Case 2", "High tariff from 18:00 to 22:00", "Flexible load should move later/earlier"),
            ("Case 3", "Appliance allowed only 10:00 to 12:00", "Window must be respected"),
            ("Case 4", "Two high-power appliances at same time", "Peak warning expected"),
            ("Case 5", "Duration longer than allowed window", "Impossible schedule must be reported"),
        ],
        "baseline": [
            "Use the appliance start times entered by the user without optimization.",
            "For every hour, add the power of all running appliances.",
            "Calculate hourly cost = load_kw x tariff_per_kwh.",
            "Add hourly costs to get daily_cost.",
            "The largest hourly load is peak_load_kw.",
            "If forecasting is included, use the previous hour or a simple moving average as baseline.",
        ],
        "screen": ("Hourly load/tariff table and appliance table", "Schedule timeline, daily cost, peak load, baseline comparison, errors"),
        "source_plan": "Use 24 one-hour slots first. Cite load/tariff sources and appliance assumptions. Later prepare at least 10,000 load records plus scheduling scenarios.",
    },
}


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverKicker", fontName="OpenSans-SemiBold", fontSize=10, leading=14, textColor=WHITE, spaceAfter=12))
styles.add(ParagraphStyle(name="CoverTitle", fontName="OpenSans-Bold", fontSize=25, leading=31, textColor=WHITE, spaceAfter=14))
styles.add(ParagraphStyle(name="CoverBody", fontName="OpenSans", fontSize=11, leading=17, textColor=WHITE, spaceAfter=8))
styles.add(ParagraphStyle(name="Kicker", fontName="OpenSans-SemiBold", fontSize=8.2, leading=11, textColor=MID, spaceAfter=4))
styles.add(ParagraphStyle(name="H1", fontName="OpenSans-Bold", fontSize=19, leading=24, textColor=BLACK, spaceAfter=10))
styles.add(ParagraphStyle(name="H2", fontName="OpenSans-SemiBold", fontSize=13, leading=17, textColor=DARK, spaceBefore=9, spaceAfter=5))
styles.add(ParagraphStyle(name="H3", fontName="OpenSans-SemiBold", fontSize=10.3, leading=14, textColor=BLACK, spaceBefore=7, spaceAfter=4))
styles.add(ParagraphStyle(name="Body", fontName="OpenSans", fontSize=9.2, leading=13.8, textColor=BLACK, spaceAfter=5))
styles.add(ParagraphStyle(name="Small", fontName="OpenSans", fontSize=8.0, leading=11.2, textColor=BLACK, spaceAfter=2))
styles.add(ParagraphStyle(name="Tiny", fontName="OpenSans", fontSize=7.2, leading=9.4, textColor=BLACK))
styles.add(ParagraphStyle(name="Center", fontName="OpenSans", fontSize=8.0, leading=11, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="CodeX", fontName="OpenSans", fontSize=7.7, leading=11.0, textColor=BLACK, leftIndent=5, rightIndent=5, spaceAfter=4))


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def box(text, shade=PALE, border=MID, style="Body"):
    t = Table([[p(text, style)]], colWidths=[17.0 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), shade),
        ("BOX", (0, 0), (-1, -1), 0.7, border),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def checklist(items, compact=False):
    style = "Tiny" if compact else "Small"
    rows = [[p("[ ]", style), p(item, style)] for item in items]
    t = Table(rows, colWidths=[0.7 * cm, 16.1 * cm], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 3 if compact else 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 if compact else 4),
    ]))
    return t


def steps_table(items):
    rows = []
    for idx, item in enumerate(items, 1):
        stage = "M1" if idx <= 5 else "M2"
        rows.append([p(str(idx), "Center"), p(stage, "Center"), p(item, "Small")])
    t = Table([[p("Step", "Small"), p("Stage", "Small"), p("What happens", "Small")]] + rows, colWidths=[1.0 * cm, 1.3 * cm, 14.7 * cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 1), (1, 5), LIGHT),
        ("BACKGROUND", (0, 6), (1, 8), PALE),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def numbered(items):
    rows = [[p(str(idx), "Center"), p(item, "Small")] for idx, item in enumerate(items, 1)]
    t = Table(rows, colWidths=[0.8 * cm, 16.2 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


class GuideDoc(BaseDocTemplate):
    def __init__(self, filename, project, **kwargs):
        self.project = project
        super().__init__(filename, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="main")
        self.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=self.page_art)])

    def page_art(self, canvas, doc):
        canvas.saveState()
        if doc.page == 1:
            canvas.setFillColor(DARK)
            canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
            canvas.setFillColor(BLACK)
            canvas.rect(0, 0, 2.0 * cm, A4[1], fill=1, stroke=0)
        else:
            canvas.setFillColor(DARK)
            canvas.rect(0, A4[1] - 0.28 * cm, A4[0], 0.28 * cm, fill=1, stroke=0)
            canvas.setStrokeColor(LINE)
            canvas.line(1.8 * cm, 1.2 * cm, A4[0] - 1.8 * cm, 1.2 * cm)
            canvas.setFont("OpenSans", 7.2)
            canvas.setFillColor(MID)
            canvas.drawString(1.8 * cm, 0.78 * cm, f"{self.project['id']} | Beginner Step 1 Guide")
            canvas.drawRightString(A4[0] - 1.8 * cm, 0.78 * cm, f"Page {doc.page}")
        canvas.restoreState()


def validation_code(project_id, fields):
    numeric = [f[0] for f in fields if any(word in f[2] for word in ("number", "percentage", "kg", "seconds", "vehicles", "years", "kW", "C"))]
    if project_id == "SC05":
        return """from pathlib import Path
import pandas as pd

DATA = Path('data')
courses = pd.read_csv(DATA / 'courses.csv')
rooms = pd.read_csv(DATA / 'rooms.csv')
slots = pd.read_csv(DATA / 'timeslots.csv')

print('courses:', courses.shape)
print('rooms:', rooms.shape)
print('timeslots:', slots.shape)

assert courses['course_id'].is_unique
assert rooms['room_id'].is_unique
assert slots['slot_id'].is_unique
assert (rooms['capacity'] > 0).all()
print('STEP 1 DATA CHECK PASSED')"""
    if project_id == "SC06":
        return """import pandas as pd

stops = pd.read_csv('data/stops.csv')
dist = pd.read_csv('data/distance_matrix.csv', index_col=0)

print('stops:', stops.shape)
print('distance matrix:', dist.shape)
assert stops['stop_id'].is_unique
assert list(dist.index) == list(dist.columns)
assert (dist.values.diagonal() == 0).all()
assert (dist.values >= 0).all()
print('STEP 1 DATA CHECK PASSED')"""
    if project_id == "SC10":
        return """import pandas as pd

load = pd.read_csv('data/hourly_load.csv')
apps = pd.read_csv('data/appliances.csv')

print('hourly rows:', len(load))
print('appliances:', len(apps))
assert len(load) == 24
assert load['hour'].between(0, 23).all()
assert (load['historical_load_kw'] >= 0).all()
assert (apps['power_kw'] > 0).all()
assert (apps['earliest_start'] < apps['latest_finish']).all()
print('STEP 1 DATA CHECK PASSED')"""
    file_name = "data/sample_input.csv"
    required = [f[0] for f in fields]
    return f"""import pandas as pd

FILE = '{file_name}'
REQUIRED = {required!r}
NUMERIC = {numeric!r}

df = pd.read_csv(FILE)
print('shape:', df.shape)
print('columns:', list(df.columns))
print('missing values:', df.isna().sum().to_dict())

missing_columns = [c for c in REQUIRED if c not in df.columns]
assert not missing_columns, f'Missing columns: {{missing_columns}}'
assert not df[REQUIRED].isna().any().any(), 'Missing value found'
for column in NUMERIC:
    assert pd.api.types.is_numeric_dtype(df[column]), f'{{column}} must be numeric'

print('STEP 1 DATA CHECK PASSED')"""


def build(project):
    detail = DETAILS[project["id"]]
    filename = OUT / f"{project['id']}-Beginner-Step-1-Guide.pdf"
    story = [
        Spacer(1, 3.0 * cm),
        p("SOFT COMPUTING CAPSTONE", "CoverKicker"),
        p(f"{project['id']}<br/>{project['title']}", "CoverTitle"),
        p("Beginner Project Guide", "CoverBody"),
        p("All steps at a glance, with a fully spoon-fed Step 1.", "CoverBody"),
        Spacer(1, 5.0 * cm),
        p("Team size: 3-4 students", "CoverBody"),
        p("Step 1 target: 3-5 working days", "CoverBody"),
        p("M1: one week before mid-semester examination", "CoverBody"),
        p("M2: one week before end-semester examination", "CoverBody"),
        PageBreak(),
        p("PROJECT IN SIMPLE WORDS", "Kicker"),
        p("What are you building?", "H1"),
        box(project["plain"], LIGHT, DARK),
        p("Who will use it?", "H2"),
        p(detail["user"]),
        p("One-sentence problem", "H2"),
        p(detail["one_sentence"]),
        p("What M1 must show", "H2"),
        p(project["m1"]),
        p("What M2 must add", "H2"),
        p(project["m2"]),
        p("Important", "H2"),
        box("M1 must be a working Product V1: input -> processing -> output. Step 1 is the preparation needed before the main fuzzy, ANN, or GA algorithm. M2 must add a real technical improvement and a deployed Product V2.", PALE, MID),
        PageBreak(),
        p("ALL STEPS AT A GLANCE", "Kicker"),
        p("Your eight-step project path", "H1"),
        steps_table(project["steps"]),
        Spacer(1, 10),
        p("Where this guide spends most of its time", "H2"),
        p("The remaining pages explain Step 1 in very small, doable actions. Finish every checkbox before starting the main algorithm."),
        box("Do not begin fuzzy rules, neural-network training, or GA optimization just because one member is excited to code. First agree on the problem, fields, units, sample data, baseline, tests, and evidence.", PALE, MID),
        PageBreak(),
        p("STEP 1 OVERVIEW", "Kicker"),
        p("What Step 1 must produce", "H1"),
        checklist([
            "A GitHub repository that every member can open.",
            "A README.md that explains the project and how the team will work.",
            "A docs/STEP-1.md project contract.",
            "A data/README.md with field meanings, units, sources, and assumptions.",
            "The correct starter data files.",
            "Twenty clean starter rows or one small, complete fixture.",
            "Five named test cases, including an invalid or impossible case.",
            "A simple baseline written as numbered rules or pseudocode.",
            "A validation program that prints PASS for valid data and rejects bad data.",
            "A simple Product V1 screen sketch.",
            "At least one meaningful Git commit from every member.",
            "A three-minute faculty demonstration.",
        ]),
        p("Suggested five-day plan", "H2"),
        numbered([
            "Day 1: create repository, add members, assign roles, and write the one-sentence problem.",
            "Day 2: define every input/output field, unit, range, category, and missing-value rule.",
            "Day 3: create the 20-row sample or small fixture; write the five test cases.",
            "Day 4: write baseline rules, validation code, screen sketch, and make member commits.",
            "Day 5: clone/run from the beginning, correct errors, and rehearse the faculty demo.",
        ]),
        PageBreak(),
        p("STEP 1A - TEAM AND REPOSITORY", "Kicker"),
        p("Create the working space", "H1"),
        p("1. One member creates a new repository. Suggested name:"),
        box(f"<b>{project['id']}-{project['title'].replace(' ', '-').replace('/', '-')}-Team-Name</b>", LIGHT, MID),
        p("2. Add all members as collaborators. Every member accepts the invitation.", "Body"),
        p("3. Add these folders and files:", "Body"),
        Preformatted("""README.md
requirements.txt
docs/STEP-1.md
data/README.md
data/sample_input.csv   # or the project-specific starter files
src/validate_data.py
notebooks/
app/
results/
report/""", styles["CodeX"]),
        p("4. Assign first responsibilities", "H2"),
    ]
    roles = Table([
        [p("Responsibility", "Small"), p("Exact Step 1 job", "Small")],
        [p("Repository", "Small"), p("Create folders, add members, and test clone/run steps.", "Small")],
        [p("Data", "Small"), p("Write fields/units, make the sample, and record sources.", "Small")],
        [p("Baseline", "Small"), p("Write simple rules and expected results for five cases.", "Small")],
        [p("Testing/UI", "Small"), p("Write validation, draw the screen, and collect evidence.", "Small")],
    ], colWidths=[4.0 * cm, 13.0 * cm])
    roles.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [roles, p("For three students, combine Repository with Testing/UI. These are first responsibilities, not permanent silos. Everyone must understand the complete Step 1."),
              p("5. If using Git commands", "H2"),
              Preformatted("""git clone REPOSITORY-URL
cd REPOSITORY-NAME
git checkout -b your-name-step1
# create or edit your assigned files
git add .
git commit -m "Describe the real work you completed"
git push -u origin your-name-step1""", styles["CodeX"]),
              box("If Git commands feel difficult, use GitHub Desktop. The required idea is the same: pull first, work on a small task, write a clear commit message, push, and let the team review.", PALE, MID),
              PageBreak(),
              p("STEP 1B - PROJECT CONTRACT", "Kicker"),
              p("Write docs/STEP-1.md", "H1"),
              p("Copy these headings into <b>docs/STEP-1.md</b>. Then replace every instruction with your team's answer."),
              Preformatted(f"""# Step 1 Project Contract

## Team and responsibilities
- Member name - first responsibility

## One-sentence problem
{detail['one_sentence']}

## User of the product
{detail['user']}

## Inputs and units
Write the field table from the next page.

## Outputs and units
{project['outputs']}

## Baseline method
Write the numbered baseline rules from this guide.

## Soft Computing method for M1
{project['m1']}

## Advanced method for M2
{project['m2']}

## Dataset/scenario sources
Add real URLs, licences, and assumptions.

## Five mandatory test cases
Copy and complete the five cases in this guide.

## Product V1 screen sketch
Insert a photo or exported image of the sketch.

## Risks and assumptions
List what may be wrong, missing, simulated, or temporary.

## Step 1 completion evidence
Add links to files, commits, and validation output.""", styles["CodeX"]),
              p("Before saving", "H2"),
              checklist([
                  "Replace generic words such as 'user' or 'data' with project-specific words.",
                  "Write units beside every number.",
                  "Mark temporary thresholds and assumptions as temporary.",
                  "Do not claim that simulated data is real data.",
                  "Do not paste a source URL without saying what information came from it.",
              ]),
              PageBreak(),
              p("STEP 1C - INPUTS AND OUTPUTS", "Kicker"),
              p("Create the data dictionary", "H1")]

    field_rows = [[p("Field", "Small"), p("Simple meaning", "Small"), p("Type/unit", "Small"), p("Starter rule", "Small")]]
    field_rows += [[p(a, "Tiny"), p(b, "Tiny"), p(c, "Tiny"), p(d, "Tiny")] for a, b, c, d in detail["fields"]]
    field_table = Table(field_rows, colWidths=[3.2 * cm, 5.2 * cm, 3.3 * cm, 5.3 * cm], repeatRows=1)
    field_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    story += [field_table,
              p("For every field, the team must answer", "H2"),
              checklist([
                  "What does this field mean in one simple sentence?",
                  "Is it a number, category, text identifier, input, target, or output?",
                  "What is its unit?",
                  "What values are allowed for the 20-row sample?",
                  "What should happen when the value is missing?",
                  "Which source or assumption justifies the final range?",
              ]),
              p("Write the outputs separately", "H2"),
              box(f"<b>Required outputs:</b> {project['outputs']}", LIGHT, MID),
              p("Source and 10,000-record plan", "H2"),
              p(detail["source_plan"]),
              box("Step 1 uses only a small sample. The final 10,000+ records/scenarios are created in Step 2, after the small sample and validation are correct.", PALE, MID),
              PageBreak(),
              p("STEP 1D - STARTER DATA", "Kicker"),
              p("Create the first sample carefully", "H1"),
              p("Do not begin with 10,000 rows. First make a small file that every member understands."),
              p("How to create the sample", "H2"),
              numbered([
                  "Create the file or files listed on the repository page.",
                  "Type the field names exactly as written in the data dictionary.",
                  "Create five rows for the mandatory cases shown below.",
                  "Add five ordinary rows with different valid values.",
                  "Add five boundary rows close to minimum or maximum values.",
                  "Add five difficult rows that combine conditions.",
                  "Keep one wrong row in a separate test file. Do not mix it into valid data.",
                  "Save as CSV using comma-separated values and a header row.",
              ]),
              p("Five mandatory starter cases", "H2")]

    sample_rows = [[p("Name", "Small"), p("Example input", "Small"), p("What to check", "Small")]]
    sample_rows += [[p(a, "Tiny"), p(b, "Tiny"), p(c, "Tiny")] for a, b, c in detail["samples"]]
    sample_table = Table(sample_rows, colWidths=[2.7 * cm, 7.8 * cm, 6.5 * cm], repeatRows=1)
    sample_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    story += [sample_table,
              p("After entering the rows", "H2"),
              checklist([
                  "Open the CSV once in a text editor and once in a spreadsheet.",
                  "Check that no heading contains an accidental space.",
                  "Check that units are not mixed inside a numeric column.",
                  "Check that categories use one spelling only.",
                  "Check that identifiers are unique.",
                  "Ask a member who did not create the file to explain three rows.",
              ]),
              PageBreak(),
              p("STEP 1E - SIMPLE BASELINE", "Kicker"),
              p("Write the comparison method", "H1"),
              p("The baseline is deliberately simple. It lets you prove later whether the Soft Computing method is better."),
              numbered(detail["baseline"]),
              p("What to save", "H2"),
              checklist([
                  "Put the numbered rules in docs/STEP-1.md.",
                  "Write the same rules as pseudocode in docs/baseline-pseudocode.md.",
                  "For each of the five mandatory cases, write the expected baseline behavior.",
                  "Mark every temporary threshold clearly.",
                  "Do not call this baseline fuzzy logic, ANN, or GA.",
              ]),
              p("Pseudocode format", "H2"),
              Preformatted("""READ one valid input row
IF the row is invalid:
    SHOW a clear error
ELSE:
    APPLY the simple rules in order
    CALCULATE the baseline output
    PRINT the output and the rule that was used
SAVE the result for later comparison""", styles["CodeX"]),
              box("Step 1 requires the baseline design and expected behavior. A complete baseline program is built in Step 3, but writing a tiny runnable version now is encouraged.", PALE, MID),
              PageBreak(),
              p("STEP 1F - VALIDATION", "Kicker"),
              p("Make the computer check your data", "H1"),
              p("Install pandas and run the starter validator. The first version checks file shape, headings, missing values, and simple data types."),
              Preformatted("""python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
pip install pandas
pip freeze > requirements.txt
python src/validate_data.py""", styles["CodeX"]),
              p("Starter content for src/validate_data.py", "H2"),
              Preformatted(validation_code(project["id"], detail["fields"]), styles["CodeX"]),
              p("Add project-specific checks", "H2"),
              checklist([
                  "Every percentage must stay inside 0 to 100.",
                  "Counts, time, distance, power, money, or rainfall cannot be negative.",
                  "Every category must match the documented spelling.",
                  "Every identifier must be unique.",
                  "The known invalid/impossible case must fail with a clear message.",
                  "The five valid mandatory cases must pass.",
              ]),
              box("Take a screenshot of one PASS result and one expected FAIL result. Save them in results/step1/.", PALE, MID),
              PageBreak(),
              p("STEP 1G - PRODUCT V1 SKETCH", "Kicker"),
              p("Draw the screen before coding it", "H1"),
              p("Use paper, PowerPoint, Figma, Canva, or a simple drawing tool. The sketch is not the final UI."),
              p("Your screen must show", "H2"),
              checklist([
                  f"Input area: {detail['screen'][0]}.",
                  "One clear Run, Recommend, Predict, or Optimize button.",
                  f"Output area: {detail['screen'][1]}.",
                  "A place for validation errors.",
                  "A place for one explanation or chart.",
                  "A visible difference between baseline output and future Soft Computing output.",
              ]),
              p("Simple wireframe to copy", "H2"),
              Preformatted("""+--------------------------------------------------+
| PROJECT TITLE                                    |
+----------------------+---------------------------+
| INPUTS               | RESULTS                   |
| [field] [value]      | Baseline: ...             |
| [field] [value]      | Soft Computing: ...       |
| [field] [value]      | Explanation: ...          |
| [ RUN / RECOMMEND ]  | [ chart or visual area ]  |
+----------------------+---------------------------+
| Validation / error message                       |
+--------------------------------------------------+""", styles["CodeX"]),
              p("Save the sketch", "H2"),
              numbered([
                  "Export or photograph the sketch clearly.",
                  "Save it as docs/product-v1-sketch.png.",
                  "Insert it in docs/STEP-1.md.",
                  "Ask one person outside the team to explain what they think the screen does.",
                  "Correct any label that the person does not understand.",
              ]),
              PageBreak(),
              p("STEP 1H - GIT EVIDENCE", "Kicker"),
              p("Make small, honest commits", "H1"),
              p("Each commit should contain one understandable improvement. Every member must make at least one commit."),
              p("Recommended commit sequence", "H2"),
              numbered([
                  f"Create repository structure for {project['id']}",
                  "Add team roles and Step 1 project contract",
                  "Define input fields, units, and validation rules",
                  f"{project['commit']}",
                  "Add five mandatory test cases",
                  "Add sample-data validation script",
                  "Add Product V1 screen sketch",
                  "Add Step 1 evidence and run instructions",
              ]),
              p("Before every push", "H2"),
              checklist([
                  "Pull the latest team version.",
                  "Run the validation program.",
                  "Check git status and add only intended files.",
                  "Write a message that says what changed.",
                  "Push your branch and ask another member to review.",
              ]),
              p("Do not do this", "H2"),
              checklist([
                  "Do not use messages such as update, changes, final, or done.",
                  "Do not upload the complete project in one last commit.",
                  "Do not commit .venv, passwords, private datasets, or personal information.",
                  "Do not overwrite another member's work without discussing it.",
              ]),
              PageBreak(),
              p("STEP 1 APPROVAL", "Kicker"),
              p("Exactly what to show faculty", "H1"),
              p("Open the repository and demonstrate the following in order."),
              numbered([
                  "Show the repository URL and collaborator list.",
                  "Open README.md and state the one-sentence problem.",
                  "Open docs/STEP-1.md and explain the user, inputs, outputs, M1, and M2.",
                  "Open data/README.md and show the field meanings, units, source links, and assumptions.",
                  "Open the sample data and point out one normal, one boundary, and one difficult row.",
                  "Run python src/validate_data.py and show PASS.",
                  "Run or show the deliberately invalid case and explain the expected error.",
                  "Explain the baseline rules and expected result for one test case.",
                  "Show the Product V1 screen sketch.",
                  "Show Git history and one meaningful commit from every member.",
              ]),
              p("Final Step 1 checklist", "H2"),
              checklist([
                  "Every required file exists and opens.",
                  "The problem boundary is small and clear.",
                  "Inputs and outputs have names, meanings, units, and rules.",
                  "The starter data is understandable and valid.",
                  "Five mandatory cases are written with expected behavior.",
                  "The simple baseline is explainable.",
                  "Validation shows both PASS and expected FAIL evidence.",
                  "The screen sketch includes input, result, explanation, and errors.",
                  "Every member has committed and can explain the work.",
              ], compact=True),
              box("After faculty approval, begin Step 2: create the reproducible 10,000+ record/scenario pipeline. Do not change field meanings or units silently; update the contract and commit the change.", LIGHT, DARK),
              PageBreak(),
              p("QUICK REFERENCE", "Kicker"),
              p("What comes after Step 1", "H1"),
              steps_table(project["steps"]),
              p("M1 finish line", "H2"),
              checklist([
                  "10,000+ cited records or documented scenarios",
                  "Working baseline",
                  "Working core Soft Computing method",
                  "Runnable Product V1",
                  "At least two useful result visuals",
                  "Interim report and M1 demonstration",
              ]),
              p("M2 finish line", "H2"),
              checklist([
                  "Advanced or hybrid method",
                  "Parameter experiments and difficult-case testing",
                  "Baseline vs M1 vs M2 comparison",
                  "Public deployment and usable interface",
                  "Final report, approximately five-minute video, presentation, and viva preparation",
              ]),
              box("A strong capstone is one that another person can open, run, understand, test, and compare.", PALE, MID)]

    doc = GuideDoc(
        str(filename),
        project,
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.45 * cm,
        bottomMargin=1.55 * cm,
        title=f"{project['id']} - {project['title']} - Beginner Step 1 Guide",
        author="Galgotias University",
        subject="Beginner-friendly Soft Computing capstone project guide",
    )
    doc.build(story)
    return filename


created = [build(project) for project in PROJECTS]
for path in created:
    print(path)
