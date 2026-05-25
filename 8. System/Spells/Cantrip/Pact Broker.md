---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Cantrip]]", "[[Concentrate]]", "[[Hex]]", "[[Linguistic]]", "[[Mental]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You offer to broker a pact of peace. If the target accepts and doesn't take hostile actions against you and your allies during the hex's duration, you take a –1 status penalty to Deception checks to Lie to them. If they refuse and take a hostile action against you or an ally during the hex's duration, they must first attempt a Will save. If they accepted the offer and then take a hostile action against you or an ally during the hex's duration, they must first attempt a Will save and treat the result as one category worse. Regardless of the outcome, the target is then temporarily immune for 1 minute.
- **Success** The target is unaffected.
- **Failure** The target takes 2d4 mental damage and a –1 status penalty to attack and damage rolls against you and your allies for the hex's duration.
- **Critical Failure** As failure, but the penalty is –2.

> [!danger] Effect: Spell Effect: Pact Broker

**Heightened (+1)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
