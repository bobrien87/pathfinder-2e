---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 45}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your skin becomes a canvas that records history as you learn it. When you receive the tattoo, choose a Lore skill. You can add the visual trait to the [[Recall Knowledge]] action in order to study your tattoos, granting you a +1 item bonus to your check using the chosen Lore skill. A storied skin tattoo starts with an icon that represents a central event in your subject of study and is usually placed on the forehead or over the heart. Each time you learn about a major event in the history of that subject, an image, design, or symbol appears on your skin to represent the event.

**Activate—Living History** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** The tattoo's design animates for 1 round, crudely portraying some scene associated with the chosen Lore skill.

**Source:** `= this.source` (`= this.source-type`)
