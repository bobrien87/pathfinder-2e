---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Agile]]", "[[Magical]]", "[[Sweep]]", "[[Thrown 10]]"]
price: "{'gp': 600}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Wielded by wealthy Taldan knights against the Goroth Lodge, this +1 striking returning hatchet has an axe head resembling a roaring lion's head.

**Activate—Slash and Burn** `pf2:r` (manipulate)

**Trigger** You critically succeed at a Strike against a plant

**Effect** The weapon's etchings pulse with green energy, as it tears through bark, leaf, and wood. The clear cutter's axe deals an additional 1d10 persistent,fire damage to the plant.

**Activate—Mow Down** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You hurl the axe horizontally, sending it flying through the air in a wild, whirling cyclone. The axe flies in a @Template[emanation|distance:30] around you, eliminating all non-magical undergrowth and any resulting difficult terrain, cover, and concealment in area. It attempts to counteract one magical effect that affects a plant in the area (counteract +20). Plant creatures in the area take 5d6 slashing damage (DC 25 [[Reflex]] save). As the axe finishes its circuit, it returns to your hand.

**Source:** `= this.source` (`= this.source-type`)
