---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Fire]]", "[[Magical]]", "[[Shove]]"]
price: "{'gp': 70000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When the mighty fire-and-metal elemental *Temperbrand* is defeated, their corpse transforms into a *+3 major striking greater flaming grievous shifting maul* made of what appears to be molten steel, though it behaves as if it were made of solid metal. When a creature first picks up *Temperbrand*, they must succeed at a DC 43 [[Will]] save to establish their dominance over the weapon. On a success, they become *Temperbrand's* only accepted wielder and may use the weapon normally. On a failure, the character takes 20d6 fire damage (40d6 fire damage on a critical failure) and drops the weapon as it melts away into slag and immediately reforms in an adjacent space. A new attempt to establish dominance can be made by picking the weapon up again and attempting a new Will save. Once *Temperbrand* has an accepted wielder, it can't be wielded by anyone else unless the accepted wielder intentionally permits it, declaring so in a loud voice; this permission can be rescinded in a similar manner. Anyone else trying to wield *Temperbrand* after it has accepted a wielder takes fire damage and causes the weapon to melt away as if they failed the Will save to wield it.

The additional fire damage caused by *Temperbrand's* greater flaming property (but not its persistent fire damage) is splash damage. *Temperbrand's* wielder is immune to this splash damage.

**Activate—Molten Smash** `pf2:1` (concentrate, manipulate)

**Frequency** once per day

**Effect** You smash *Temperbrand* against the ground or another solid adjacent surface, causing an explosion of molten metal and force to radiate outward in a @Template[emanation|distance:20]. All creatures in this area take 10d6 fire damage and 6d6 force damage (DC 43 [[Reflex]] save); those who critically fail this save are knocked [[Prone]]. You are immune to the effects of Molten Smash, but your allies are not.

**Source:** `= this.source` (`= this.source-type`)
