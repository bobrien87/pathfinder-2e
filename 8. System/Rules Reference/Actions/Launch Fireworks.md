---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Cost** 1 versatile vial

**Requirements** You're holding or wearing an [[Alchemist's Toolkit]] and have a free hand

**Effect** You set off a fireworks display. You can launch a normal firework to simply create a visual or audible signal within 20 feet or you can choose one of the following special effects. You can also use the comet, flower, or salute fireworks displays, and feats can add more options. A specific fireworks display takes the listed number of actions to launch and has the listed traits.

**Comet** `pf2:1` (visual) You shoot a streak of shining light in a @Template[line|distance:60]. All spaces in that line are lit with bright light until the start of your next turn. As part of this action, you can also [[Point Out]] a single creature in the line, and your allies do not need to hear or understand you.

**Flower** `pf2:1` (visual) You ignite a ring of sparks, creating a shape that might be reminiscent of a flower blooming in the sky. Each enemy in a @Template[emanation|distance:20] must attempt a [[Fortitude]] save. On a failure, the enemy is [[Dazzled]] for 1 round, and on a critical failure they are dazzled for 2 rounds.

**Salute** `pf2:1` (auditory) You create a startling bang or whistle. When you launch a salute display, you can choose a [[Confused]] or [[Fascinated]] ally within 60 feet. If the ally you chose is fascinated, the noise is so violent that it acts as a hostile effect for the purpose of their fascinated condition (though it has no negative repercussions) automatically ending most applications of the fascinated condition. If they're confused, the sound is so loud and violent that it might snap the ally out of confusion. They can immediately attempt the flat check to remove the confused condition which normally occurs when a creature is damaged. If the confused condition has special rules that remove the flat check when taking damage or make the flat check harder, those rules also apply to the salute.

**Source:** `= this.source` (`= this.source-type`)
