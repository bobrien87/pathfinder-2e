---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:3`"
range: "30 feet"
duration: "1 hour"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure an intricate vehicle, carved entirely from wood, to serve as a method of conveyance. The vehicle appears in an unoccupied area of your choice within range. The vehicle can be piloted using Arcana, Driving Lore, or Nature skill checks. The DC to pilot the vehicle and the DC of the vehicle's collision are equal to your spell DC. The vehicle's remaining statistics are presented below.

When you Cast this Spell, choose whether to create a Large skiff, a Large wagon, or a Medium cycle. With the GM's permission, you might instead summon a different vehicle of your choice with a maximum level of 1; this vehicle must be made primarily of plant matter, have common rarity, and be Large or smaller.

- **Large Skiff—Space** 15 feet long, 5 feet wide, 3 feet high; **Crew** 1 pilot; **Passengers** 3; **Speed** swim 30 feet (magical)

- **Large Wagon—Space** 10 feet long, 10 feet wide, 7 feet high; **Crew** 1 pilot; **Passengers** 3; **Speed** 35 feet (magical)

- **Medium Cycle—Space** 5 feet long, 3 feet wide, 3 feet high; **Crew** 1 pilot; **Passengers** 0; **Speed** 40 feet (magical)

**AC** 13; **Fortitude** +8

**Hardness** 5, **HP** 40 (BT 20); **Immunities** critical hits, object immunities, precision damage; **Weaknesses** fire 5, slashing 5

**Collision** 2d6

**Heightened (+1)** The vehicle's AC increases by 2, Fortitude bonus increases by 2, Hardness increases by 1, HP increases by 20, and the collision damage increases by `r 1d6`. In addition, the maximum level of vehicle you can summon with GM permission increases by 2. The duration increases by 1 hour.

**Source:** `= this.source` (`= this.source-type`)
