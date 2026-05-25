---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Propulsive]]"]
price: "{'gp': 1250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This is a *+2 striking sling* made from the neck, jaw, and tongue of a mobogo to resemble its mouth. The tongue curls around each bullet, which is thrown with the snap of your wrist. Each throw causes a small croak to echo from the sling.

**Activate—Bolstering Croak** `pf2:2` (auditory, concentrate, emotion, manipulate, mental)

**Frequency** once per day;

**Effect** You raise your sling and work the handle to mimic a mobogo's croaking song. Allies within @Template[emanation|distance:25]{25 feet} gain a +1 status bonus to saves against fear effects for 1 round. You can Sustain this for up to 4 rounds. During this time, you can't use the sling to Strike or activate its Tongue Twister ability. After using Bolstering Croak, you can recharge it once per day by feeding the sling a number of gallons of water equal to double the number of rounds for which the Bolstering Croak was active. For example, if you activated but didn't sustain Bolstering Croak, you would require 2 gallons of water to recharge it. If you activated Bolstering Cloak and then Sustained for 1 round, you would require 4 gallons of water.

> [!danger] Effect: Bolstering Croak

**Activate—Tongue Twister** `pf2:2` (manipulate)

**Requirements** The sling isn't loaded

**Effect** You fully unfurl the sling's tongue to grab hold of a creature within 20 feet, and attempt to move them. Attempt an [[Athletics]] check against the creature's Fortitude DC. On a success, you can move the creature up to 15 feet into any space within 20 feet of you. If you target a willing ally with this ability, you automatically succeed at the Athletics check.

**Craft Requirements** The initial raw materials must include the throat, tongue, and skin from a mobogo.

**Source:** `= this.source` (`= this.source-type`)
