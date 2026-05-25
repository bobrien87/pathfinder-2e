---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'gp': 100}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A drake rifle is a firearm made from the saliva glands of a drake. The firearm launches small bursts of empowered spittle instead of typical rounds of ammunition. A drake rifle is a +1 weapon. It's a distinct type of martial firearm that deals 1d10 cold damage with a range increment of 150 feet and reload 1. On a critical hit, the spittle clings to the target and they take persistent damage of the same type as the weapon equal to @Damage[(1d4 + @item.system.damage.dice)[persistent,@item.system.damage.damageType]]{1d4 + the number of weapon damage dice}. A drake rifle does not add critical specialization effects.

**Activate—Drake Shot** `pf2:3` (manipulate)

**Frequency** once per day

**Effect** You fire a large, specialized burst designed to hamper your foes. Make a ranged Strike with the drake rifle. As long as the Strike isn't a critical failure, the drake rifle deals @Damage[(1 * @item.system.damage.dice[splash])[@item.system.damage.damageType]]{1 splash damage per weapon damage die} to the target and creatures within @Template[burst|distance:5]{5 feet} of the target. This splash damage is of the same type as its normal damage.

On a hit, the drake rifle provides one of the following additional effects based on its damage type:

- **Cold** Frozen spittle clings to the target. The target takes a –10-foot status penalty to their Speeds for 1 minute (

> [!danger] Effect: Drake Rifle (Cold)

).

**Craft Requirements** The initial raw materials must include the saliva glands of a ritually hunted drake with a breath weapon that deals the appropriate damage type for the drake rifle

**Source:** `= this.source` (`= this.source-type`)
