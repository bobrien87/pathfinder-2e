---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 10000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** A character who is a member of the Knights of Lastwall has access to this weapon.

These *+2 greater striking vitalizing longswords* are granted as special commendations to Knights of Lastwall who perform acts of exceptional heroism or strike decisive blows against the forces of the Whispering Tyrant.

**Activate—Comes the Dawn** `pf2:r` (concentrate, divine, healing, vitality)

**Frequency** once per day

**Trigger** You regain Hit Points from a magical effect

**Effect** You release a wave of vital energy in a @Template[type:emanation|distance:30]. For every 10 Hit Points you are healed, you restore 1d10 Hit Points to all other living creatures and deal that amount of vitality damage to all undead creatures in the area, with a DC 37 [[Fortitude]] save.

**Source:** `= this.source` (`= this.source-type`)
