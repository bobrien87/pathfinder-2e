---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Divine]]", "[[Grimoire]]"]
price: "{'gp': 425}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Script in a language of the Outer Planes adorns this book's spine, and a deity's symbol is etched on its cover. *Books of warding prayers* are each devoted to a particular deity and are also a religious symbol of that deity.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** Your last action was to cast a prepared divine spell granted by your deity

**Effect** You and all your allies in a @Template[type:emanation|distance:30] gain resistance 10 to spirit damage for 1 minute. You can instead choose to grant resistance to holy effects instead of spirit damage if the spell you cast had the holy trait, or resistance to unholy effects instead of spirit if your spell had the unholy trait.

> [!danger] Effect: Book of Warding Prayers

**Source:** `= this.source` (`= this.source-type`)
