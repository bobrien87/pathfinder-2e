---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1300}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Valued among soldiers (particularly those from war-torn Nirmathas) who often find themselves operating undercover, this large-collared garment is reminiscent of a highwayman's coat. A *skirmisher's coat* is cleverly constructed, and contains several concealed pockets and grants the wearer a +2 item bonus to checks made to [[Conceal an Object]].

**Activate—Costume Change** `pf2:1` (concentrate, illusion)

**Effect** You change the shape and appearance of all your clothing, making them appear as ordinary or fine clothes of your imagining. This doesn't change the statistics of any armor you're wearing. Only a creature that's benefiting from [[Truesight]] or a similar effect can attempt to disbelieve this illusion, with a DC of 28.

**Activate—Unexpected Armament** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You reach into one of the coat's pockets and withdraw a chunk of metal that instantly expands into a common simple or martial melee weapon of your choice. The weapon functions as a +1 striking weapon. When you produce the weapon, you decide if it is made from cold iron or silver, and which one of the following property runes it gains: *corrosive*, *flaming*, *frost*, *shock*, or *thundering*. This weapon remains for 1 hour or until it leaves your grasp, at which point it vanishes.

**Source:** `= this.source` (`= this.source-type`)
