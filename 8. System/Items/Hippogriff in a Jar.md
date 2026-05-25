---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This bottle contains a shrunken hippogriff. When opened, the contents reconstitute into a Large effigy of a hippogriff. The hippogriff waits up to 1 round and allows two creatures to mount it, then Flies up to 65 feet and waits 1 more round to give the mounted creatures time to dismount. Creatures who are still mounted on the hippogriff when it dissolves fall [[Prone]] in the space where the hippogriff corpse ends its movement.

**Craft Requirements** Supply the corpse of a hippogriff.

**Source:** `= this.source` (`= this.source-type`)
