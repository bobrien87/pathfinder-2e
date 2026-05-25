---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Artifact]]", "[[Magical]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When the runelord of greed Gimmel summoned and briefly controlled the Oliphaunt of Jandelay, he set into motion events he couldn't have guessed, and the aftermath of the visitation would forever change Golarion. Neither the forces of Azlant nor Thassilon could challenge the Oliphaunt once it broke free of Gimmel's control, but that doesn't mean it didn't leave behind some small part of itself—a fragment of one of its teeth that served as a sort of seed, promising an eventual apocalypse in the land's far future. It was this tooth fragment that first drew the Ashen Man's attention to Golarion so long ago.

The *Apocalypse Seed* might be but a fragment of one of the Oliphaunt's teeth, but it's still as large as a barrel. The huge chunk of ivory retains a jagged edge on the side where it broke off. Otherwise, it's unblemished and of an unsettling yellow tint in coloration. Sometimes, when caught on the edge of one's peripheral vision, the surface seems covered with writhing spiral sigils, but they fade from view if directly observed. The first time a creature touches the *Apocalypse Seed*, they hear phantom sounds of titanic footsteps and the far-off trumpet of annihilation, drawing inexorably closer for a few moments before the sensation fades, never to be repeated for that creature again.

**Activate—Oliphaunt's Cry** `pf2:2` (concentrate, manipulate, sonic)

**Effect** Spend 1 Mythic Point. You summon the echo of the Oliphaunt's trumpeting blast, creating a @Template[type:cone|distance:120] of sound. Each creature in the area must attempt a DC 45 [[Fortitude]] save with the following effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes @Damage[5d10[sonic]|options:area-damage] damage and is [[Deafened]] for 1 round.
- **Failure** The creature takes @Damage[10d10[sonic]|options:area-damage] damage, is [[Slowed]] 1 for 2 rounds, and is deafened for 2 rounds.
- **Critical Failure** The creature takes @Damage[20d10[sonic]|options:area-damage] damage, is [[Slowed]] 2 for 2 rounds, and is deafened for 4 rounds.

**Destruction** The *Apocalypse Seed* is destroyed if it's returned to Jandelay and thrown into the Oliphaunt's mouth. This lifts the promised apocalypse from Golarion and makes it impossible for the Oliphaunt to ever return to this world unless a new *Apocalypse Seed* is created and buried somewhere on Golarion.

**Source:** `= this.source` (`= this.source-type`)
