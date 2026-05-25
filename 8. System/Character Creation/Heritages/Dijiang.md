---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Sprite|Sprite]]"
traits: ["[[Sprite]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have the form of a faceless, leathery ball with short fur, six legs, and a connection to primordial chaos. While you have no face, head, mouth, eyes, or ears, you can somehow hear, speak, see, eat, and breathe just fine (though it's unclear exactly how). Your erratic nature means you often react to stimuli in unpredictable ways.

When you roll a failure (though not a critical failure) on a saving throw against an emotion effect, you get a success instead.

**Source:** `= this.source` (`= this.source-type`)
