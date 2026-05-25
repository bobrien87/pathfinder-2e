---
type: item
source-type: "Remaster"
level: "23"
traits: ["[[Artifact]]", "[[Backstabber]]", "[[Concussive]]", "[[Fatal d12]]", "[[Kickback]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The barrel of this long rifle is translucent in places, forming a swirled pattern along the metal, and its stock is formed of crimson wood. *Ghosthand's Comet* is a *+4 major striking beast-bane greater impactful advanced firearm* with a range increment of 300 feet. It deals 5d8 force damage and has the backstabber, concussive, kickback, and fatal d12 traits. As a star gun, Ghosthand's Comet runs on magic and doesn't use ammunition or black powder. The weapon is silent when fired.

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a ranged Strike with *Ghosthand's Comet*

**Effect** For the triggering Strike, *Ghosthand's Comet* changes its damage type to your choice of acid, cold, electricity, fire, or sonic.

**Activate** `pf2:1` (concentrate)

**Effect** On your next attempt at a ranged Strike with *Ghosthand's Comet*, the shot phases through any material or magical obstacle, such as a wall of force, in its path, ignoring all cover. You must attempt the Strike by the end of your turn or this effect is lost.

**Destruction** If the Grim Reaper slays the wielder of *Ghosthand's Comet*, the Reaper's scythe, as it strikes the killing blow, is destined to slice the star gun in half.

**Source:** `= this.source` (`= this.source-type`)
