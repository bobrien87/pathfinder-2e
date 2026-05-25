---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Censer]]", "[[Fire]]", "[[Magical]]", "[[Poison]]"]
price: "{'gp': 2750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The exterior of this egg-shaped brass censer is polished to a mirror-like sheen. Several rings are attached to its sides at regular intervals. The top of the censer's lid is decorated with a pair of intertwining snakes.

**Activate—Light Incense** `pf2:2` (aura, manipulate)

**Frequency** once per day

**Cost** incense worth at least 5 gp

**Effect** A piping, reddish smoke pours from the censer in a @Template[emanation|distance:20]. You choose whether the smoke causes the target's blood to turn extremely hot or transmutes to poison; the smoke deals your choice of fire or poison damage. Each living creature that's in the area or enters it attempts a DC 34 [[Fortitude]] save saving throw, then becomes temporarily immune for 1 hour.
- **Critical Success** The creature is unaffected.
- **Success** The creature breathes in a small amount of the poisonous smoke and takes 2d6 persistent,fire or 2d6 persistent,poison damage.
- **Failure** The creature gulps down a lungful of the smoke, taking 4d6 persistent,fire or 4d6 persistent,poison damage and becoming [[Enfeebled]] 2 until the persistent damage ends.
- **Critical Failure** The creature inhales a large amount of the smoke, taking 6d6 persistent,fire or 6d6 persistent,poison damage and becoming [[Enfeebled]] 3 until the persistent damage ends.

**Source:** `= this.source` (`= this.source-type`)
