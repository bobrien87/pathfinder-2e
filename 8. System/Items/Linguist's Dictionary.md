---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 650}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thick book has several colorful bookmarks and page dividers. Its title and text shift between numerous languages.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Requirements** Your last action was to cast a spell prepared from this grimoire that allows understanding of another language, such as [[Translate]] or [[Truespeech]]

**Effect** The grimoire absorbs knowledge of one language translated this way (caster's choice if more than one), allowing its bearer to communicate on a rudimentary level in that language even after the spell's duration has elapsed. The linguist's dictionary can hold one language at a time.

**Source:** `= this.source` (`= this.source-type`)
