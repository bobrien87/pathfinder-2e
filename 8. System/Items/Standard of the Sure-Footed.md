---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Air]]", "[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 1200, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner gleams a brilliant orange with steel-gray embellishments. While holding a standard of the sure-footed, you can use the following ability.

**Activate—Help Up** `pf2:1` (air, concentrate)

**Frequency** once per turn

**Effect** A gust of wind gives an ally a helpful lift. An ally within the banner's aura can Stand as a free action.

**Source:** `= this.source` (`= this.source-type`)
