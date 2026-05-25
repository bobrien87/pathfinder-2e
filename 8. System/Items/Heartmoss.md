---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Healing]]", "[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 55}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This burgundy moss grows in heart-shaped clumps and releases a pleasant, calming scent. The spell DC of any spell cast by Activating this item is 17.

- **Armor** You gain resistance 2 to mental damage and a +1 item bonus to saving throws against effects with the emotion trait.

- **Weapon** After you cast a healing spell by activating the heartmoss, the weapon exudes a soothing scent. Your Strikes with the affixed weapon have the nonlethal trait for 1 minute. Until the end of your next turn, Strikes with the affixed weapon cause the target to be [[Stupefied 1]] for 1 round if it hits (or for 3 rounds on a critical hit).

**Activate** Cast a Spell

**Effect** You cast [[Stabilize]].

**Source:** `= this.source` (`= this.source-type`)
