---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 465, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner has an intricately embroidered pattern of shards and cracks across its surface, almost like a broken mirror. Though it always feels dry to the touch, this banner from a distance gleams red as if slightly stained with the blood of your enemies. While holding a banner of piercing shards, you can use the following ability.

**Activate—Shards Seek Wounds** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** Shards of sharpened glass violently shoot out from the magical banner into the newly opened wounds of a nearby enemy. The magical banner deals 1d4 persistent,bleed damage to any enemy within the banner's aura that has been dealt damage since the end of your last turn.

**Source:** `= this.source` (`= this.source-type`)
