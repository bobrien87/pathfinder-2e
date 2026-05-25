---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 1200, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A *spellslasher* is made of faceted crystal, its edges sharp and oddly misaligned. When it's applied to a weapon, it attunes the weapon to magical energies, allowing it to slice through spells as though they were physical threads. While your weapon is under the effect of a *spellslasher*, you gain the Spellslash reaction; you can use this reaction only with the affected weapon, and the *spellslasher*'s effects end as soon as you use Spellslash.

**Spellslash** R (magical, manipulate)

**Trigger** You are the only target of a spell

**Effect** You swing or shoot your weapon to intercept the magic, attempting to counteract the spell. Your counteract rank is equal to half your level (rounded up), and your counteract check modifier is equal to your attack modifier with the affected weapon.

**Source:** `= this.source` (`= this.source-type`)
