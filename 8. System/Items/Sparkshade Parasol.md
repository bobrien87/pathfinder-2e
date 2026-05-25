---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Fire]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large magical parasol shields you from the heat in hot environments, no matter whether the heat comes from above, like the beating sun, or below, like roiling lava. While holding the *sparkshade parasol*, you gain resistance 10 to fire and are protected from mild, severe, and extreme environmental heat.

**Activate—Parasol's Protection** R (manipulate)

**Trigger** You're targeted by or inside the area of an effect that deals fire damage

**Frequency** once per 10 minutes

**Effect** You hold your parasol between yourself and the incoming flames, gaining fire resistance 20 against the triggering effect. (This applies only to any damage the effect deals.) For the next 1 minute, flames dance harmlessly along the parasol's brim, letting you use Parasol's Pyrotechnics.

**Activate—Parasol's Pyrotechnics** `pf2:2` (concentrate, manipulate)

**Requirements** Flames are dancing on the *sparkshade parasol* due to you using Parasol's Protection

**Effect** You release captured flames out from your parasol, shooting fire in a @Template[line|distance:30]. Each creature in the line takes 10d6 fire damage (DC 28 [[Reflex]] save). This activation loses its charge.

**Source:** `= this.source` (`= this.source-type`)
