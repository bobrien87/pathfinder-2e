---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Healing]]", "[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 1750}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This burgundy moss grows in heart-shaped clumps and releases a pleasant, calming scent. The spell DC of any spell cast by Activating this item is 29.

- **Armor** You gain resistance 10 to mental damage and a +1 item bonus to saving throws against effects with the emotion trait.

- **Weapon** After you cast a healing spell by activating the heartmoss, the weapon exudes a soothing scent. Your Strikes with the affixed weapon have the nonlethal trait for 1 minute. Until the end of your next turn, Strikes with the affixed weapon cause the target to be [[Stupefied 3]] for 1 round if it hits (or for 3 rounds on a critical hit).

**Activate** Cast a Spell

**Effect** You cast [[Stabilize]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 3rd-rank [[Heal]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 4th-rank [[Sound Body]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Healing Well]].

**Source:** `= this.source` (`= this.source-type`)
