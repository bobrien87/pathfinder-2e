---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Deadly d8]]", "[[Disarm]]", "[[Finesse]]", "[[Poison]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Within hives of giant bees, some become protectors of their hive and etch runes onto their stingers via dance. Upon such a bee's death, its stinger can be removed from its body and used as *+1 striking rapier*, though a hilt often needs to be attached for skilled swordsmanship. The imbued magic allows the stinger to slowly renew a small bit of its venom supply. The wielder can gather this and deliver it during a Strike. The victim is made to see prophetic flashes of their future as it courses through their system.

**Activate—Apiprophecy Sting** `pf2:f` (manipulate)

**Frequency** once per day

**Effect** The *protector's final gift* secrets apiprophecy venom, which coats the blade and affects the next creature successfully struck with the blade within the next minute.

**Apiprophecy Venom** (poison)

**Saving Throw** DC 20 [[Will]] save

**Maximum Duration** 4 rounds

**Stage 1** 2d6 mental damage and [[Dazzled]]

**Source:** `= this.source` (`= this.source-type`)
