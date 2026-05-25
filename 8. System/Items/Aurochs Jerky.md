---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 80}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Interact

Aurochs meat already makes for tough jerky, but with the right alchemical treatment, it becomes legendarily resilient and imparts that durability to those who eat it. Eating the jerky causes a pair of inch-long horns to grow from your forehead (or causes your existing horns to grow noticeably) for 1 hour. During this time, you gain a +1 item bonus to Fortitude saves. You can end the effect prematurely, causing the horns to retract or revert to their normal size, with a free action that has the concentrate trait.

> [!danger] Effect: Aurochs Jerky

**Aurochs' Endurance** `pf2:f` (concentrate)

**Trigger** You begin your turn and are [[Fatigued]]

**Effect** You suppress the fatigued condition for 10 minutes. During this time, you are not immune to fatigue and can become fatigued by subsequent effects, but you gain a +2 item bonus to saving throws against effects that would fatigue you.

> [!danger] Effect: Aurochs' Endurance

**Source:** `= this.source` (`= this.source-type`)
