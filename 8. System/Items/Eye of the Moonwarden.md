---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 620}"
usage: "wornnecklace"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This beaded pendant crafted by Lyrune-Quah shamans features an uncut moonstone that warns the wearer of danger. When a hostile creature comes within 30 feet of you, the stone glows with moonlight only you can see.

**Activate—Lunar Illumination** `pf2:1` (concentrate)

**Frequency** once per hour

**Effect** Bright moonlight shines out of the gem in a @Template[type:emanation|distance:30], forcing hostile creatures in the area to make a DC 26 [[Fortitude]] save or be [[Blinded]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
