---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Alchemist]]", "[[Concentrate]]", "[[Manipulate]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You have fewer than your maximum number of versatile vials, and you're either holding or wearing an alchemist's toolkit.

You scrounge together enough ingredients from what's left in your alchemist's toolkit to produce a few more versatile vials on the fly. Attempt a [[Crafting]] check. The DC is usually a standard-difficulty DC for your level, but the GM can assign a different DC based on the circumstances. The number of vials you regain depends on the result of your check (up to your maximum).
- **Critical Success** You regain 3 versatile vials.
- **Success** You regain 2 versatile vials.
- **Failure** You regain 1 versatile vial.
- **Critical Failure** You don't regain any versatile vials.

**Source:** `= this.source` (`= this.source-type`)
