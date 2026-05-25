---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]"]
price: "{'gp': 9000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This device is made from two metal discs, one slightly smaller than the other, each bearing a variety of runes and symbols along their outer edges. The center ring typically shows a rune for each elemental plane, and many older ciphers include only the planes of air, earth, fire, and water. A thick, golden pin in the center of both discs holds them together.

**Activate - Align to Plane** a (manipulate, scrying, visual)

**Effect** You turn the discs to align symbols, creating a minute planar gateway as large as a keyhole. You can look through it to view a location in an elemental plane. Each cipher connects to 12 locations on each elemental plane-typically large settlements. Anyone holding the cipher can understand the primary language of the plane the cipher is aligned to. A cipher of the planes can be used in place of a planar key for [[Interplanar Teleport]] and similar magic for travel to the plane it's aligned to. When it's used this way, you arrive unerringly at the location the cipher is aligned to.

**Source:** `= this.source` (`= this.source-type`)
