---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A vial of this *enigma-sight potion* seems to contain fragments of kaleidoscopic crystal that reflect mind-bending scenes. However, these "crystals" act like liquid when poured or consumed. Drinking the potion grants you the effects of a [[Truesight]] spell, except that you use your Perception modifier and half your level, rounded up, for the secret counteract check instead of the normal counteract modifier and spell rank. However, if you critically fail the secret counteract check the effect grants, your mind fills in false, nightmarish information. You become [[Stupefied 1]] for 1d4 rounds and [[Stunned]] 1 as your brain struggles to process what you see.

**Source:** `= this.source` (`= this.source-type`)
