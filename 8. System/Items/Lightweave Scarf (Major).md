---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Spellheart]]", "[[Visual]]"]
price: "{'gp': 22000}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The first of these strips of glittering cloth was worn by a monk from Jinin who would interweave it into his *handwraps of mighty blows*. The spell DC of any spell cast by activating this item is 38.

- **Armor** You gain a +3 item bonus to saving throws against illusions and Deception checks to [[Create a Diversion]].
- **Weapon** (visual) After you cast an illusion spell by activating the scarf, the weapon is shrouded in a mesmerizing illusory pattern. Your next Strike causes the target to be [[Confused]] for 1 minute if it hits. If you don't make a Strike by the end of your next turn, the illusion ends with no effect.

> [!danger] Effect: Lightweave Scarf (Armor)

**Activate** Cast a Spell

**Effect** You cast [[Light]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 8th-rank [[Vibrant Pattern]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Confusing Colors]].

**Source:** `= this.source` (`= this.source-type`)
