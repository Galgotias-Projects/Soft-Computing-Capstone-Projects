from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Soft-Computing-Beginner-Project-Start-Guide.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

RED = colors.HexColor("#B5121B")
DARK_RED = colors.HexColor("#7F0D14")
PALE_RED = colors.HexColor("#FFF2F3")
NAVY = colors.HexColor("#17324D")
PALE_BLUE = colors.HexColor("#EEF5FA")
GREEN = colors.HexColor("#287A4B")
PALE_GREEN = colors.HexColor("#EDF8F1")
AMBER = colors.HexColor("#A55B00")
PALE_AMBER = colors.HexColor("#FFF7E8")
INK = colors.HexColor("#20252B")
MID = colors.HexColor("#5B6670")
LIGHT = colors.HexColor("#D8DEE4")
WHITE = colors.white


PROJECTS = [
    {
        "id": "SC01",
        "title": "Intelligent Campus Climate and Energy Controller",
        "plain": "Build a small app that looks at room conditions and suggests how much cooling and fan speed are needed. It should also avoid wasting energy when the room is empty or electricity is expensive.",
        "m1": "A fuzzy controller for one room, compared with a simple temperature-rule controller.",
        "m2": "Use a Genetic Algorithm (GA) to improve the fuzzy settings, test difficult weather cases, and deploy the app.",
        "steps": [
            "Choose one room and define its inputs and outputs.",
            "Create and validate climate and occupancy scenarios.",
            "Build a simple fixed-threshold controller.",
            "Build the fuzzy controller and explain its rules.",
            "Join everything in a working Product V1 screen.",
            "Use GA to tune membership functions or rules.",
            "Compare fixed, fuzzy, and GA-fuzzy results.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": [
            "data/sample_input.csv",
            "data/README.md",
            "docs/STEP-1.md",
            "src/validate_data.py",
        ],
        "columns": "scenario_id, temperature_c, humidity_pct, occupancy_count, tariff_level",
        "ranges": "Temperature 18-45 C; humidity 20-100%; occupancy 0 to room capacity; tariff low, medium, or high.",
        "outputs": "cooling_pct (0-100), fan_level (off/low/medium/high), energy_action (normal/save/avoid_peak)",
        "baseline": "Use simple temperature bands for cooling. Increase fan speed when humidity is high. If occupancy is zero, use minimum operation.",
        "cases": [
            "Comfortable occupied room",
            "Hot and humid occupied room",
            "Empty room",
            "Heat wave with high tariff",
            "Cool room with high humidity",
        ],
        "commit": "Define climate input schema and five test cases",
    },
    {
        "id": "SC02",
        "title": "Smart Washing Machine Decision and Resource Optimizer",
        "plain": "Build an app that recommends wash time, water, detergent, and spin speed after the user describes the clothes and water availability.",
        "m1": "A fuzzy washing controller, compared with fixed washing presets.",
        "m2": "Use GA to balance washing quality with water, detergent, and energy use, then deploy the app.",
        "steps": [
            "Choose the washing machine capacity and define inputs.",
            "Create and validate realistic washing scenarios.",
            "Build fixed wash-cycle presets.",
            "Build fuzzy variables, rules, and outputs.",
            "Join the controller and screen as Product V1.",
            "Use GA to tune quality and resource trade-offs.",
            "Test delicate, scarce-water, and heavy-load cases.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/sample_input.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "scenario_id, dirt_score, load_kg, fabric_type, water_availability_pct",
        "ranges": "Dirt score 0-10; load 0.5 kg to machine capacity; fabric delicate/cotton/synthetic/heavy; water 0-100%.",
        "outputs": "wash_time_min, water_litre, detergent_ml, spin_rpm",
        "baseline": "Create one fixed preset for every fabric type. The preset does not change with dirt or water availability.",
        "cases": [
            "Lightly soiled half-load",
            "Heavily soiled full cotton load",
            "Delicate fabric",
            "Low-water situation",
            "Overloaded input that must be rejected",
        ],
        "commit": "Add validated sample wash scenarios",
    },
    {
        "id": "SC03",
        "title": "Student Performance and Academic Intervention System",
        "plain": "Build a decision-support app that identifies a student's academic risk level and suggests a helpful intervention. It must use anonymous data and must not punish a student automatically.",
        "m1": "One transparent neural classifier and a simple score baseline, shown in a risk and intervention screen.",
        "m2": "Compare Perceptron, ADALINE, and Backpropagation; study errors, imbalance, fairness, and deploy the app.",
        "steps": [
            "Define anonymous inputs, risk labels, and interventions.",
            "Prepare and validate a cited student dataset.",
            "Build a score-threshold or majority baseline.",
            "Build one neural classifier and show its learning.",
            "Create the risk and intervention Product V1.",
            "Add and compare the other neural methods.",
            "Study errors, imbalance, noise, and fairness.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/sample_input.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "record_id, attendance_pct, assessment_pct, assignment_pct, engagement_score, prior_performance_pct, risk_label",
        "ranges": "Percentages 0-100; engagement 0-10; risk label low, medium, or high. Do not store names or phone numbers.",
        "outputs": "risk category and one clear intervention, such as monitor, mentor, or faculty follow-up",
        "baseline": "Use a visible weighted score and simple thresholds. Write down the temporary weights and explain that they must be tested.",
        "cases": [
            "Consistently strong student",
            "Low attendance only",
            "Weak marks and assignments",
            "High engagement but weak prior performance",
            "Contradictory or boundary record",
        ],
        "commit": "Document anonymous academic-risk schema",
    },
    {
        "id": "SC04",
        "title": "Adaptive Traffic Signal Optimization System",
        "plain": "Build a small traffic-junction simulator. The app should choose which direction gets green and for how long, using queue and waiting-time information.",
        "m1": "A fuzzy controller for one two-phase junction, compared with a fixed-time signal.",
        "m2": "Use GA to tune the controller, test emergencies and heavy queues, and deploy the simulator.",
        "steps": [
            "Define one simple two-phase junction.",
            "Generate and validate traffic states.",
            "Build the fixed-time signal and queue updates.",
            "Build fuzzy phase priority and green duration.",
            "Create the working junction Product V1.",
            "Use GA to tune controller parameters.",
            "Compare controllers in difficult traffic cases.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/sample_input.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "state_id, queue_ns, queue_ew, density_ns_pct, density_ew_pct, max_wait_ns_sec, max_wait_ew_sec, emergency_direction",
        "ranges": "Queues cannot be negative; density 0-100%; wait 0-300 seconds; emergency direction none, NS, or EW.",
        "outputs": "next_phase (NS/EW) and green_duration_sec, with safe minimum and maximum values",
        "baseline": "Alternate north-south and east-west using a fixed 30-second green time.",
        "cases": [
            "Balanced low traffic",
            "Heavy north-south queue",
            "Heavy east-west queue",
            "Long wait but shorter queue",
            "Emergency vehicle override",
        ],
        "commit": "Document fixed-time traffic baseline",
    },
    {
        "id": "SC05",
        "title": "University Timetable Optimization Engine",
        "plain": "Build a program that places courses into rooms and time slots without clashes. It should also try to reduce gaps and respect preferences.",
        "m1": "A Genetic Algorithm timetable for a small test case, compared with random or greedy placement.",
        "m2": "Add more objectives and constraints, test larger cases, improve the interface, and deploy it.",
        "steps": [
            "Define courses, rooms, faculty, slots, and constraints.",
            "Create reusable timetable fixtures and variations.",
            "Build a random or greedy scheduler.",
            "Build the GA and a repair or penalty method.",
            "Create a timetable viewer as Product V1.",
            "Add multi-objective constraints.",
            "Compare GA settings at different problem sizes.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/courses.csv", "data/rooms.csv", "data/timeslots.csv", "data/constraints.md", "src/validate_data.py"],
        "columns": "courses: course_id, cohort_id, faculty_id, weekly_sessions, duration_slots, required_room_type; rooms: room_id, capacity, room_type; timeslots: slot_id, day, start_time, end_time",
        "ranges": "Start with 5 courses, 3 rooms, 3 faculty members, 2 cohorts, and 10 time slots.",
        "outputs": "course_id, room_id, slot_id, faculty_id, cohort_id, plus hard-violation and soft-penalty counts",
        "baseline": "Place each course in the first available valid slot, or use random placement with retry.",
        "cases": [
            "Feasible timetable",
            "Room shortage",
            "Faculty clash",
            "Cohort clash",
            "Preference conflict with no hard violation",
        ],
        "commit": "Add timetable entities and clash fixtures",
    },
    {
        "id": "SC06",
        "title": "Multi-Stop Campus Shuttle or Delivery Route Optimizer",
        "plain": "Build an app that finds a good order for visiting campus stops. It should reduce distance or time while respecting priorities and later time windows.",
        "m1": "A permutation GA route, compared with the nearest-neighbour method, with a route display.",
        "m2": "Add traffic, priorities, and time windows; compare methods; and deploy the app.",
        "steps": [
            "Choose the depot, stops, and route rules.",
            "Create distances and route scenarios.",
            "Build the nearest-neighbour baseline.",
            "Build the permutation GA.",
            "Create the route Product V1 with charts.",
            "Add traffic, priorities, and time windows.",
            "Compare routes in difficult cases.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/stops.csv", "data/distance_matrix.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "stop_id, stop_name, x_coordinate, y_coordinate, priority, earliest_time, latest_time",
        "ranges": "Use one depot and 6-10 stops. The distance from a stop to itself must be zero. Explain any one-way distance.",
        "outputs": "visit order, total distance, estimated time, and total penalty or cost",
        "baseline": "From the current stop, always visit the nearest stop that has not yet been visited.",
        "cases": [
            "Ordinary six-stop route",
            "Two equally close stops",
            "High-priority distant stop",
            "Congested connection",
            "Impossible or narrow time window",
        ],
        "commit": "Add campus stops and distance checks",
    },
    {
        "id": "SC07",
        "title": "Smart Irrigation and Crop Water Management System",
        "plain": "Build an app that recommends when and how much to irrigate after looking at soil, weather, rainfall, and crop stage.",
        "m1": "An ANN water predictor or a complete fuzzy irrigation controller, compared with a fixed moisture threshold.",
        "m2": "Combine ANN prediction with fuzzy decisions, test difficult sensor and weather cases, and deploy the app.",
        "steps": [
            "Choose one crop and one growing context.",
            "Prepare and validate weather and soil data.",
            "Build the fixed moisture-threshold baseline.",
            "Build the ANN or fuzzy M1 method.",
            "Create the irrigation Product V1.",
            "Combine ANN and fuzzy components.",
            "Compare methods and stress-test sensors.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/sample_input.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "scenario_id, soil_moisture_pct, humidity_pct, temperature_c, rainfall_mm, crop_stage",
        "ranges": "Moisture and humidity 0-100%; rainfall cannot be negative; crop stage initial/development/mid/late.",
        "outputs": "water_requirement_litre or mm, irrigation_duration_min, decision off/low/medium/high",
        "baseline": "Turn irrigation on when soil moisture is below one fixed threshold. Turn it off after sufficient rain.",
        "cases": [
            "Dry and hot",
            "Adequate moisture",
            "Recent heavy rain",
            "Dry soil with high humidity",
            "Impossible or noisy sensor reading",
        ],
        "commit": "Define irrigation units and sample scenarios",
    },
    {
        "id": "SC08",
        "title": "Machine Predictive Maintenance and Fault Priority System",
        "plain": "Build a dashboard that reads machine sensor values, estimates fault risk, and tells the maintenance team how urgently the machine needs attention.",
        "m1": "An ANN fault-risk model or fuzzy priority controller, compared with crisp sensor thresholds.",
        "m2": "Combine ANN risk with fuzzy severity, test noisy and extreme readings, and deploy the dashboard.",
        "steps": [
            "Choose the machine observation and fault target.",
            "Prepare and validate cited sensor data.",
            "Build crisp sensor-threshold rules.",
            "Build the ANN or fuzzy M1 method.",
            "Create the maintenance Product V1.",
            "Combine ANN risk and fuzzy priority.",
            "Test imbalance, noise, and extreme readings.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/sample_input.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "reading_id, vibration, temperature_c, rpm, load_pct, severity, fault_label",
        "ranges": "Copy vibration and RPM units from one chosen dataset. Do not mix units. Load is 0-100%.",
        "outputs": "fault_probability, risk_band (low/medium/high), maintenance_priority (routine/soon/immediate)",
        "baseline": "Use a small set of visible sensor thresholds. Mark temporary thresholds and later justify them with sources or data.",
        "cases": [
            "Normal operation",
            "High vibration only",
            "Overheating under high load",
            "Several severe signals",
            "Missing or noisy sensor value",
        ],
        "commit": "Document sensor units and fault labels",
    },
    {
        "id": "SC09",
        "title": "Intelligent Loan or Credit Risk Decision Support System",
        "plain": "Build an educational decision-support app that estimates credit risk and explains a recommended action. Use only public, anonymous data.",
        "m1": "An ANN risk classifier, compared with a visible score-threshold baseline.",
        "m2": "Use fuzzy logic for borderline cases, check calibration and fairness, and deploy the app.",
        "steps": [
            "Define anonymous inputs, target, and recommendation.",
            "Prepare and validate a public credit dataset.",
            "Build a transparent score baseline.",
            "Build the ANN classifier and show its errors.",
            "Create the risk Product V1.",
            "Add fuzzy handling for borderline cases.",
            "Compare accuracy, calibration, and fairness.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/sample_input.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "record_id, income, loan_amount, debt_to_income_pct, repayment_history, employment_length, credit_target",
        "ranges": "State currency and units. Explain every category and missing-value rule. Never collect real financial details from classmates.",
        "outputs": "risk_band, confidence, recommended_action (review/approve/reject)",
        "baseline": "Give points for a few documented features, add the points, and use visible thresholds for risk bands.",
        "cases": [
            "Low debt and stable history",
            "High debt",
            "Borderline score",
            "Strong income but poor repayment history",
            "Missing or unknown category",
        ],
        "commit": "Document anonymous credit schema and ethics",
    },
    {
        "id": "SC10",
        "title": "Smart Energy Demand and Appliance Scheduling System",
        "plain": "Build an app that predicts electricity demand and chooses good times to run appliances so that cost and peak load are reduced.",
        "m1": "An ANN forecast or GA scheduler MVP, compared with an original non-optimized schedule.",
        "m2": "Combine ANN forecasting with GA scheduling, test tariffs and preferences, and deploy the app.",
        "steps": [
            "Choose one home, lab, or small building.",
            "Prepare hourly load, tariff, and appliance data.",
            "Build the original schedule or forecast baseline.",
            "Build the ANN forecast or GA scheduler.",
            "Create the energy Product V1.",
            "Combine ANN forecasting and GA scheduling.",
            "Compare cost and peaks in difficult cases.",
            "Deploy Product V2 and finish all evidence.",
        ],
        "files": ["data/hourly_load.csv", "data/appliances.csv", "data/README.md", "docs/STEP-1.md", "src/validate_data.py"],
        "columns": "hourly_load: date, hour, historical_load_kw, temperature_c, tariff_per_kwh; appliances: appliance_id, power_kw, duration_slots, earliest_start, latest_finish, interruptible, priority",
        "ranges": "Use 24 one-hour slots. Power, energy, tariff, and time-window units must be written clearly.",
        "outputs": "forecast_load_kw, appliance start slots, daily_cost, peak_load_kw",
        "baseline": "Keep the original user-entered appliance times. If forecasting, use persistence or a simple moving average.",
        "cases": [
            "Normal tariff",
            "Expensive evening peak",
            "Narrow appliance time window",
            "Two high-power appliances competing",
            "Impossible schedule that must be flagged",
        ],
        "commit": "Add 24-hour energy and appliance fixtures",
    },
]


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=27, leading=32, textColor=WHITE, alignment=TA_LEFT, spaceAfter=14))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["BodyText"], fontName="Helvetica", fontSize=13, leading=19, textColor=WHITE, spaceAfter=8))
styles.add(ParagraphStyle(name="Kicker", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=RED, spaceAfter=5))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=DARK_RED, spaceBefore=4, spaceAfter=10))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13.5, leading=17, textColor=NAVY, spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle(name="H3x", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=7, spaceAfter=4))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=14.1, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.1, leading=11, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name="Tinyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.3, leading=9.4, textColor=INK))
styles.add(ParagraphStyle(name="CenterSmall", parent=styles["Smallx"], alignment=TA_CENTER))
styles.add(ParagraphStyle(name="Callout", parent=styles["Bodyx"], fontName="Helvetica-Bold", fontSize=10, leading=15, textColor=INK, spaceAfter=0))


def p(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def box(text, background=PALE_BLUE, border=NAVY, style="Bodyx"):
    table = Table([[p(text, style)]], colWidths=[17.1 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), 0.8, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return table


def checklist(items):
    rows = [[p("[ ]", "Smallx"), p(item, "Smallx")] for item in items]
    table = Table(rows, colWidths=[0.7 * cm, 16.2 * cm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def compact_checklist(items):
    cells = []
    for item in items:
        cells.append(p(f"[ ] {item}", "Tinyx"))
    if len(cells) % 2:
        cells.append(p("", "Tinyx"))
    rows = [cells[index:index + 2] for index in range(0, len(cells), 2)]
    table = Table(rows, colWidths=[8.45 * cm, 8.45 * cm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.25, LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def numbered(items):
    rows = [[p(str(i), "CenterSmall"), p(item, "Smallx")] for i, item in enumerate(items, 1)]
    table = Table(rows, colWidths=[0.75 * cm, 16.15 * cm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), PALE_RED),
        ("TEXTCOLOR", (0, 0), (0, -1), DARK_RED),
        ("BOX", (0, 0), (-1, -1), 0.4, LIGHT),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


class GuideDoc(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=self.draw_page)])

    def draw_page(self, canvas, doc):
        canvas.saveState()
        if doc.page == 1:
            canvas.setFillColor(RED)
            canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
            canvas.setFillColor(DARK_RED)
            canvas.rect(0, 0, 2.1 * cm, A4[1], fill=1, stroke=0)
        else:
            canvas.setFillColor(RED)
            canvas.rect(0, A4[1] - 0.35 * cm, A4[0], 0.35 * cm, fill=1, stroke=0)
            canvas.setStrokeColor(LIGHT)
            canvas.line(1.8 * cm, 1.25 * cm, A4[0] - 1.8 * cm, 1.25 * cm)
            canvas.setFillColor(MID)
            canvas.setFont("Helvetica", 7.5)
            canvas.drawString(1.8 * cm, 0.82 * cm, "Soft Computing Capstone | Beginner Project Start Workbook")
            canvas.drawRightString(A4[0] - 1.8 * cm, 0.82 * cm, f"Page {doc.page}")
        canvas.restoreState()


def project_pages(project):
    story = [PageBreak()]
    story += [
        p(f"PROJECT {project['id']}", "Kicker"),
        p(project["title"], "H1x"),
        box(f"<b>In simple words:</b> {project['plain']}", PALE_RED, RED),
        Spacer(1, 8),
        p("What you must finish", "H2x"),
    ]
    phase = Table([
        [p("M1 - Working Product V1", "Callout"), p(project["m1"], "Smallx")],
        [p("M2 - Better Product V2", "Callout"), p(project["m2"], "Smallx")],
    ], colWidths=[4.5 * cm, 12.4 * cm])
    phase.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), PALE_BLUE),
        ("BACKGROUND", (0, 1), (0, 1), PALE_GREEN),
        ("BOX", (0, 0), (-1, -1), 0.5, LIGHT),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 7),
    ]))
    story += [phase, p("Your eight steps", "H2x"), numbered(project["steps"])]
    story += [
        Spacer(1, 7),
        box("<b>Do not jump ahead.</b> First complete Step 1 below. Do not start the main fuzzy, ANN, or GA code until the team can show the Step 1 evidence.", PALE_AMBER, AMBER),
        PageBreak(),
        p(f"{project['id']} - STEP 1 WORKSHEET", "Kicker"),
        p("Do this first", "H1x"),
        p("A beginner team can finish this in three to five working days. Divide the work, but discuss every item together.", "Bodyx"),
        p("1. Create these files", "H2x"),
        checklist([f"Create <b>{name}</b>." for name in project["files"]]),
        p("2. Put these columns in the sample data", "H2x"),
        box(f"<b>Columns:</b> {project['columns']}<br/><br/><b>Starter rules:</b> {project['ranges']}", PALE_BLUE, NAVY, "Smallx"),
        p("3. Write the expected output", "H2x"),
        p(project["outputs"]),
        p("4. Write the simple baseline", "H2x"),
        p(project["baseline"]),
        p("5. Create exactly 20 sample rows", "H2x"),
        p("Begin with only 20 rows. Include normal, boundary, and difficult rows. Your validation program must print the file shape, column names, missing-value count, and invalid values. After this works, you may plan the required 10,000 or more records/scenarios."),
        p("6. Include these five test cases", "H2x"),
        checklist(project["cases"]),
        p("7. Make small Git commits", "H2x"),
        box(f"Example commit: <b>{project['commit']}</b><br/>Every member must make at least one meaningful commit. Do not upload the complete project in one final commit.", PALE_GREEN, GREEN, "Smallx"),
        p("Stop and show this to faculty", "H2x"),
        compact_checklist([
            "Repository works; all members have access.",
            "STEP-1 explains the problem, inputs, outputs, M1, and M2.",
            "Field names, units, ranges, and missing-value rules are written.",
            "The 20-row sample loads without errors.",
            "One deliberately wrong row is rejected.",
            "Five named test cases are present.",
            "Baseline rules and a Product V1 screen sketch are included.",
            "Every member can run and explain the validation program.",
        ]),
    ]
    return story


story = [
    Spacer(1, 3.3 * cm),
    p("GALGOTIAS UNIVERSITY", "CoverSub"),
    p("Soft Computing Capstone", "CoverTitle"),
    p("Beginner Project Start Workbook", "CoverTitle"),
    Spacer(1, 0.4 * cm),
    p("A step-by-step guide for students who are new to GitHub, datasets, algorithms, and software projects.", "CoverSub"),
    Spacer(1, 1.0 * cm),
    p("Use this workbook before writing the main algorithm.", "CoverSub"),
    Spacer(1, 5.2 * cm),
    p("Team size: 3-4 students", "CoverSub"),
    p("M1: finish one week before the mid-semester examination", "CoverSub"),
    p("M2: finish one week before the end-semester examination", "CoverSub"),
    PageBreak(),
    p("START HERE", "Kicker"),
    p("How to use this workbook", "H1x"),
    box("<b>You are not expected to know everything on day one.</b> Follow one small action at a time. Save evidence after every action. Ask for faculty review after Step 1, before building the main algorithm.", PALE_GREEN, GREEN),
    p("For every project", "H2x"),
    numbered([
        "Read the complete project specification once. Do not code while reading.",
        "Read the two-page section for your project in this workbook.",
        "Create the repository and Step 1 files.",
        "Prepare only 20 clean sample rows first.",
        "Write the simple baseline and five test cases.",
        "Run the validation program and correct every error.",
        "Show the Step 1 checklist to faculty.",
        "After approval, continue with Steps 2-5 for M1 and Steps 6-8 for M2.",
    ]),
    p("Important words", "H2x"),
]

word_table = Table([
    [p("Word", "Callout"), p("Simple meaning", "Callout")],
    [p("Repository", "Smallx"), p("The main project folder stored on GitHub.", "Smallx")],
    [p("Commit", "Smallx"), p("A saved checkpoint with a short message explaining what changed.", "Smallx")],
    [p("Dataset", "Smallx"), p("A table of examples used to build or test the project.", "Smallx")],
    [p("Scenario", "Smallx"), p("One possible situation given to the program, such as a hot occupied room.", "Smallx")],
    [p("Baseline", "Smallx"), p("A simple method used for comparison. Your advanced method should improve on it.", "Smallx")],
    [p("Validation", "Smallx"), p("Checks that data is present, correctly named, and inside allowed limits.", "Smallx")],
    [p("Input / output", "Smallx"), p("Inputs go into the program. Outputs are the decisions or predictions returned by it.", "Smallx")],
], colWidths=[3.6 * cm, 13.3 * cm], repeatRows=1)
word_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), RED),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("GRID", (0, 0), (-1, -1), 0.35, LIGHT),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("PADDING", (0, 0), (-1, -1), 6),
]))
story += [word_table, PageBreak(), p("THE COMMON PLAN", "Kicker"), p("Eight steps from start to final product", "H1x")]

roadmap = [
    ("1", "M1", "Freeze the project contract", "Choose the exact user, problem, inputs, outputs, units, baseline, data source, five test cases, repository, and responsibilities."),
    ("2", "M1", "Build the data pipeline", "Collect or generate 10,000+ cited records/scenarios. Clean, validate, prepare, and split them so another person can repeat the work."),
    ("3", "M1", "Implement the baseline", "Build the simple comparison method and save its results."),
    ("4", "M1", "Implement the main M1 technique", "Make the required fuzzy, ANN, or GA method work and show its important internal steps."),
    ("5", "M1", "Assemble Product V1", "Connect input, validation, baseline, main method, output, and at least two visuals in one runnable screen."),
    ("6", "M2", "Add the advanced technique", "Add optimization, a hybrid model, more algorithms, priorities, or multiple objectives."),
    ("7", "M2", "Experiment and stress-test", "Compare baseline, M1, and M2. Change parameters and test noise, extremes, unseen cases, and impossible constraints."),
    ("8", "M2", "Finish Product V2", "Improve and deploy the app. Finish the report, video, presentation, README, and viva preparation."),
]
road_table = Table(
    [[p("Step", "Callout"), p("Stage", "Callout"), p("Work", "Callout"), p("Meaning", "Callout")]]
    + [[p(a, "CenterSmall"), p(b, "CenterSmall"), p(c, "Smallx"), p(d, "Smallx")] for a, b, c, d in roadmap],
    colWidths=[1.0 * cm, 1.2 * cm, 4.4 * cm, 10.3 * cm],
    repeatRows=1,
)
road_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), RED),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("BACKGROUND", (0, 1), (1, 5), PALE_BLUE),
    ("BACKGROUND", (0, 6), (1, 8), PALE_GREEN),
    ("GRID", (0, 0), (-1, -1), 0.35, LIGHT),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("PADDING", (0, 0), (-1, -1), 6),
]))
story += [road_table, Spacer(1, 8), box("<b>M1 is not a proposal.</b> Product V1 must accept input, perform processing, and show useful output. <b>M2 is not only a prettier screen.</b> Product V2 must contain a real technical improvement, experiments, deployment, and final evidence.", PALE_AMBER, AMBER)]

story += [PageBreak(), p("STEP 1 FOR EVERY TEAM", "Kicker"), p("Set up the project correctly", "H1x")]
story += [p("A. Create the repository", "H2x"), p("Use a clear repository name, such as <b>SC01-Climate-Controller-Team-A</b>. Add every team member as a collaborator. Create the structure below."),
          box("<font name='Courier'>project-repository/<br/>|-- README.md<br/>|-- requirements.txt<br/>|-- docs/<br/>|   `-- STEP-1.md<br/>|-- data/<br/>|   |-- README.md<br/>|   `-- sample_input.csv<br/>|-- notebooks/<br/>|-- src/<br/>|-- app/<br/>|-- results/<br/>`-- report/</font>", colors.HexColor("#F7F8FA"), MID, "Smallx"),
          p("B. Give every member a first responsibility", "H2x")]

role_table = Table([
    [p("Responsibility", "Callout"), p("First job", "Callout")],
    [p("Repository and integration", "Smallx"), p("Create folders, add members, and keep the run instructions correct.", "Smallx")],
    [p("Data and scenarios", "Smallx"), p("Define fields and units, create the 20-row sample, and write data-source information.", "Smallx")],
    [p("Baseline and algorithm", "Smallx"), p("Write the simple baseline and draw the future algorithm flow.", "Smallx")],
    [p("Interface, testing, and evidence", "Smallx"), p("Draw the screen, write five test cases, and save screenshots/results.", "Smallx")],
], colWidths=[5.2 * cm, 11.7 * cm], repeatRows=1)
role_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("GRID", (0, 0), (-1, -1), 0.35, LIGHT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("PADDING", (0, 0), (-1, -1), 6),
]))
story += [role_table, p("For a three-person team, one person may combine repository work with interface/testing. Everyone must still understand the complete project.", "Smallx"),
          p("C. Put these headings in docs/STEP-1.md", "H2x"),
          box("<font name='Courier'># Step 1 Project Contract<br/>## Team and responsibilities<br/>## One-sentence problem<br/>## User of the product<br/>## Inputs and units<br/>## Outputs and units<br/>## Baseline method<br/>## Soft Computing method for M1<br/>## Advanced method for M2<br/>## Dataset/scenario sources<br/>## Five mandatory test cases<br/>## Product V1 screen sketch<br/>## Risks and assumptions<br/>## Step 1 completion evidence</font>", colors.HexColor("#F7F8FA"), MID, "Smallx")]

story += [PageBreak(), p("STEP 1 FOR EVERY TEAM", "Kicker"), p("Prepare evidence before the main algorithm", "H1x"),
          p("D. Make an input and output dictionary", "H2x"),
          p("For every field, write its name, simple meaning, type, unit, allowed range or category, missing-value rule, data source, and whether it is an input, target, or output."),
          p("E. Make a small 20-row sample", "H2x"),
          numbered(["Create the correct column headings.", "Add ordinary rows.", "Add boundary rows near the minimum and maximum.", "Add difficult or contradictory rows.", "Add one deliberately wrong row in a separate test file.", "Run validation and correct every unexpected error."]),
          p("F. Write the baseline before the advanced method", "H2x"),
          p("The baseline is a simple rule, threshold, greedy method, or average. It gives you something fair to compare with the fuzzy, ANN, or GA solution."),
          p("G. Draw one Product V1 screen", "H2x"),
          checklist(["Input area", "Run / Recommend / Optimize button", "Baseline output", "Soft Computing output", "One explanation or chart", "Validation and error-message area"]),
          p("H. Save work with meaningful commits", "H2x"),
          box("Good messages: <b>Define input fields and units</b>; <b>Add 20 validated scenarios</b>; <b>Document baseline rules</b>; <b>Add invalid-input test</b>.<br/><br/>Weak messages: <b>update</b>; <b>final</b>; <b>changes</b>; <b>project complete</b>.", PALE_GREEN, GREEN, "Smallx"),
          p("Common beginner mistakes", "H2x"),
          checklist(["Do not copy code that nobody in the team can explain.", "Do not download data without saving its URL and licence.", "Do not create 10,000 bad rows before 20 rows work correctly.", "Do not build only slides or a report for M1.", "Do not wait until the last day to create the GitHub repository.", "Do not let one member upload all work in one commit."])]

for project in PROJECTS:
    story.extend(project_pages(project))

story += [PageBreak(), p("FACULTY REVIEW", "Kicker"), p("Step 1 submission checklist", "H1x"),
          p("A team should be able to demonstrate all items below in about three minutes."),
          checklist([
              "Repository URL works and all team members are collaborators.",
              "Required folders, README.md, and requirements.txt exist.",
              "docs/STEP-1.md is complete in simple language.",
              "Input/output dictionary includes units and validation rules.",
              "data/README.md contains real source URLs and licence information.",
              "A valid 20-row sample fixture is present.",
              "Five named test cases include a boundary or error case.",
              "Baseline pseudocode or rule table is present.",
              "Product V1 screen sketch is visible.",
              "A script or notebook loads and validates the sample.",
              "Every member has made a meaningful commit.",
              "Every member can explain the problem, input, output, baseline, M1, and M2.",
          ]),
          Spacer(1, 8),
          box("<b>Step 1 is not complete</b> when a team has only copied the problem statement, created slides, downloaded an undocumented dataset, or uploaded all work at once.", PALE_RED, RED),
          p("What happens after Step 1 approval?", "H2x"),
          numbered(["Expand the data plan and create the reproducible 10,000+ record/scenario pipeline.", "Implement and measure the simple baseline.", "Implement the M1 Soft Computing method.", "Join data, baseline, method, output, and visuals into Product V1.", "Prepare the M1 demo one week before the mid-semester examination."]),
          PageBreak(), p("FINAL REMINDER", "Kicker"), p("Build, test, explain, and show evidence", "H1x"),
          box("A strong capstone is not the project with the most complicated words. It is the project that another person can open, run, understand, test, and compare.", PALE_GREEN, GREEN),
          p("Before every faculty review", "H2x"),
          checklist(["Pull the latest repository version.", "Follow your own setup instructions from the beginning.", "Run one normal case and one error case.", "Open the latest results and screenshots.", "Check that every chart has a title, labels, units, and explanation.", "Ask every member to explain one code part and one result."]),
          p("Submission timing", "H2x"),
          numbered(["M1 Working Product V1: finish one week before the mid-semester examination.", "M2 Advanced Product V2: finish one week before the end-semester examination."]),
          Spacer(1, 18), p("Team notes", "H2x")]

notes = Table([[p("", "Smallx")] for _ in range(8)], colWidths=[17.0 * cm], rowHeights=[1.0 * cm] * 8)
notes.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.5, LIGHT)]))
story.append(notes)


doc = GuideDoc(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=1.8 * cm,
    leftMargin=1.8 * cm,
    topMargin=1.45 * cm,
    bottomMargin=1.55 * cm,
    title="Soft Computing Capstone - Beginner Project Start Workbook",
    author="Galgotias University",
    subject="Step-by-step capstone guidance for absolute beginners",
)
doc.build(story)
print(OUTPUT)
