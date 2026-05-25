---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
traits: ["[[Consecration]]"]
cast: "3 days"
range: "40 feet"
area: "40-foot burst"
duration: "1 year"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 40-foot-radius burst around an immobile altar, shrine, or fixture of your deity

**Secondary Casters** 2, must be worshippers of your religion

You consecrate a site to your deity, chanting praises and creating a sacred space. While within the area, worshippers of your deity gain a +1 status bonus to attack rolls, skill checks, saving throws, and Perception checks, and creatures anathema to your deity (such as undead for Pharasma or Sarenrae) take a -1 status penalty to those rolls. If your deity's divine sanctification allows you to choose holy or unholy, you can choose to make the consecrated site holy or unholy as well. If the deity's sanctification *must* be holy or unholy, you must make the site match that sanctification. Strikes made by worshippers of your deity within the area gain the site's sanctification trait, if any.
- **Critical Success** The consecration succeeds, and it either lasts for 10 years instead of 1 or covers an area with twice the radius. Occasionally, with your deity's favor, this might produce an even more amazing effect, such as a permanently consecrated area or the effect covering an entire cathedral.
- **Success** The consecration succeeds.
- **Failure** The consecration fails.
- **Critical Failure** The consecration fails spectacularly and angers your deity, who sends a sign of displeasure. For at least 1 year, further attempts to consecrate the site fail.

**Heightened (7th)** The consecrated area also gains the effects of the *planar seal* spell, but the effect doesn't attempt to counteract teleportation by worshippers of your deity. The cost increases to 200 gp × the spell rank.

**Source:** `= this.source` (`= this.source-type`)
