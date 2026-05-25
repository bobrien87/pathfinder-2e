---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gogiteth"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Sakvroth ((Can't Speak))"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +24, Stealth +21, Survival +17"
abilityMods: ["+6", "+3", "+4", "-2", "+1", "+0"]
abilities_top:
  - name: "Carry Off Prey"
    desc: "The gogiteth can move at its full Speed while it has a creature [[Grabbed]] in its jaws, bringing the grabbed creature along."
armorclass:
  - name: AC
    desc: "31 all-around vision; **Fort** +25, **Ref** +22, **Will** +20"
health:
  - name: HP
    desc: "250; **Resistances** poison 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Skittering Reposition"
    desc: "`pf2:r` **Trigger** A creature that starts its move outside the gogiteth's reach moves into its reach. <br>  <br> **Effect** The gogiteth moves 10 feet. This does not trigger reactions."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (unarmed), **Damage** 3d10+12 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Leg +26 (`pf2:1`) (agile, reach 10 ft.), **Damage** 3d6+12 piercing"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d6+12)[bludgeoning]], DC 32 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Skittering Assault"
    desc: "`pf2:2` The gogiteth Strides three times. Once per Stride, it can attempt a leg Strike against a creature in its reach at any point during the Stride; it must make each attack against a different creature, but it doesn't apply its multiple attack penalty until after making all its Strikes. If any of the Strikes result in a critical failure, Skittering Assault ends."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A gogiteth is a slavering nightmare of teeth, eyes, and hairy spiderlike legs, and its appearance is invariably seared into the minds of any who witness it. Hives of these skittering monsters haunt the lowest reaches of the Darklands, competing with cave worms and other subterranean horrors for food and resources. A gogiteth is rarely alone, as they learned that the best means of survival is sticking with others of their own kind. Even the hardiest Darklands residents seek cover when a gogiteth is spotted, for where there's one, a swarm is sure to follow.

Gogiteths make a clacking sound as they skitter. The joints in their many legs pop and crack with each movement, though they can suppress this voluntarily and hunt silently without alerting prey. The odd creatures can also make a high-pitched whistling sound that echoes throughout the caverns where they live. Some Darklands natives report that groups of gogiteths sometimes join together in eerie, discordant songs.

Gogiteth anatomy have inspired no shortage of speculation as to their origins. Some believe they are the result of a fleshwarping experiment gone horribly wrong. Others think they may be related in some way to the Dominion of the Black—possibly the distant cousins or some strange exiles of those alien entities. According to this mythos, once they made their way to Golarion, the gogiteths crawled into the depths of the earth, shying away from the blazing sun above.

Gogiteths are a menace to every other denizen of the Darklands. Those who live in gogiteth-infested regions of Sekamina or Orv frequently call for temporary truces when a gogiteth swarm has been spotted. Since even an average gogiteth hive can host up to two dozen of the horrors, calls to eradicate them are dangerous quests indeed.

```statblock
creature: "Gogiteth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
