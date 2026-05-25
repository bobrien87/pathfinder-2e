---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 35}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Perhaps you had no other choice than to steal the boots off a fallen soldier. Yours may have been worn out, full of holes, or even coming apart. Did you take them from a fallen ally or adversary? Everyone looks the same after war has its way. Nevertheless, the guilt you feel weighs you down. You gain a +1 item bonus to saving throws and DCs against forced movement.

**Activate—One of You** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You shuffle your boots, which still stink of the dead, causing one undead creature of your choice to think that you too are undead. The target is [[Off Guard]] against the next melee attack you attempt against it before the end of your current turn.

**Source:** `= this.source` (`= this.source-type`)
