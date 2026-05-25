---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Illusion]]", "[[Occult]]", "[[Shadow]]", "[[Visual]]", "[[Wayang]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You move your body in a pattern that evokes the small and clever Sister Mousedeer, misdirecting enemies and filling their vision with shadows to hide behind. Attempt a Performance check against the Perception DC of a single enemy within 30 feet. This has all the usual traits and restrictions of a Performance check. You can affect up to two targets within range if you have expert proficiency in Performance, four if you have master proficiency, and eight if you have legendary proficiency.
- **Critical Success** Imaginary shadows rise up in the target's vision, hiding you from sight. You gain greater cover against that enemy, which provides a +4 circumstance bonus to AC and to Stealth checks to Hide, [[Sneak]], or otherwise avoid detection. As the shadows are illusory, you don't gain the typical bonus to Reflex saves from greater cover. These benefits last until the beginning of your next turn, or until you move from your current space, use an attack action, or become [[Unconscious]], whichever comes first.
- **Success** As critical success, except you gain only standard cover (a +2 circumstance bonus instead).
- **Critical Failure** The opponent grasps the movements of your dance, becoming temporarily immune to your Dance of the Mousedeer for 1 day.

**Source:** `= this.source` (`= this.source-type`)
