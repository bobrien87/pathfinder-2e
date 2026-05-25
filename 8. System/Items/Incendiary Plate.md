---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Bulwark]]", "[[Fire]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 70000}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bright-red *+3 greater resilient full plate* is adorned with eerily beautiful, angry flames that flow and glow with your movement, making it appear as if you are engulfed in a living fire. You gain resistance 10 to fire while wearing this armor.

**Activate—Living Flame** `pf2:2` (aura, concentrate, fire)

**Frequency** once per day

**Effect** The armor engulfs you in a vortex of living fire in a @Template[type:emanation|distance:15] for 10 minutes. Creatures that enter this aura or start their turn within it take @Damage[10d6[fire]|options:area-damage|traits:aura,concentrate,fire] damage (DC 40 [[Reflex]] save). This area is difficult terrain for other creatures.

**Source:** `= this.source` (`= this.source-type`)
