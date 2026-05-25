---
type: item
source-type: "Remaster"
level: "4"
price: "{'gp': 80}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made with a brightly colored leather strap, these goggles have a series of overlapping lenses in an array of colors spanning the spectrum of visible light. The effect of this is that every color is more vibrant and similar shades have higher contrast. This means that shapes of even similar colors tend to stand out more, allowing the wearer to see even camouflage easier. As an Interact action, you can set the lenses to make things stand out at your current location. Until you move, you gain a +1 item bonus to Perception checks when you [[Seek]].

**Source:** `= this.source` (`= this.source-type`)
