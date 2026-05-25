---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Clockwork]]"]
price: "{'gp': 600}"
usage: "other"
bulk: "20"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The printing press is a revolutionary machine that combines movable type with a mechanical inking system and screw press, allowing for the mass production of large volumes of text. Using the press, a worker can produce up to 3,600 identical pages per day. In order to use the printing press, you must first set the type for the page you want to print. Time required to set type varies depending on the number of characters used; from 1 hour for small pages with brief text, to 8 hours for a full-sized normal page of text, though extreme examples may be outside this range. When you prepare a page for printing, you can include engraved images in addition to text. No magical properties of text are transferred in the printing process, so it cannot be used to mass-produce magical scrolls, spellbooks, or similar spells or magic items.

**Source:** `= this.source` (`= this.source-type`)
