---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 15}"
usage: "worneyeglasses"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Theater enhancers* resemble a pair of opera glasses. When worn, they allow the viewer to see subtle illusions on key props or stage elements that have been cast ahead of time. For instance, a puppet of a demon might appear to project a sinister moving shadow, or a backdrop of a mountain might have snowflakes falling over it. Popular among theatergoers who want a visual experience grander than what they can see with their own eyes, *theater enhancers* are largely limited to fancy stage productions that can afford the time and money it takes to enchant a stage with them in mind.

**Source:** `= this.source` (`= this.source-type`)
