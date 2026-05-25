---
type: creature
group: ["Beast", "Ethereal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ether Spider"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Ethereal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Athletics +12, Stealth +15"
abilityMods: ["+5", "+4", "+3", "-2", "+1", "+7"]
abilities_top:
  - name: "Ether Spider Venom"
    desc: "**Saving Throw** DC 22 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** 2d6 poison damage, [[Clumsy]] 2 and [[Slowed]] 1 (1 round) <br>  <br> **Stage 3** 3d6 poison damage, [[Clumsy]] 3 and [[Slowed]] 2 (1 round)"
  - name: "Ethereal Web Trap"
    desc: "A creature hit by the ether spider's web attack is [[Immobilized]] and stuck to the nearest surface ([[Escape]] DC 22)."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +15, **Will** +10"
health:
  - name: HP
    desc: "75"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +15 (`pf2:1`) (magical), **Damage** 1d10+7 piercing plus [[Ether Spider Venom]] plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Web +14 (`pf2:1`) (magical, range 30 ft.), **Damage**  plus [[Ethereal Web Trap]]"
spellcasting: []
abilities_bot:
  - name: "Ethereal Step"
    desc: "`pf2:1` The ether spider shifts to either the Ethereal Plane or the Universe. The ether spider can remain on the Ethereal Plane indefinitely without ill effect. While there, it can see clearly into the Universe with a range of 60 feet. On its first round in an encounter, the ether spider can use this ability once as a free action."
  - name: "Web Burst"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The ether spider flings a gout of stored webs in a @Template[type:cone|distance:30]. These webs can pass between the Universe and the Ethereal Plane. Each creature in the area is [[Immobilized]], as ethereal web trap, unless it succeeds at a DC 22 [[Reflex]] save."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Ether spiders are members of a vague taxonomy called ethereal wildlife and are deadly predators from the Ethereal Plane. They are giant arachnids who can shape the raw essence of the Ethereal Plane as easily as spinning silk, weaving it in complex patterns that drift through the misty void. From these ethereal nests, whole families of ether spiders can scout adjacent locales in the Universe, watching for easy prey in dark or remote corners of the land of mortals. Once an ether spider has spotted a meal, it anchors its nest and waits on the Ethereal Plane for its prey to draw near. As soon as its victim is within reach, the ether spider shifts to the Universe, clamps its fangs onto its prey, then shifts back to the Ethereal Plane to wait as its venom works through the creature's system. Ether spiders move between the planes with ease, making them extremely dangerous to those who can't see or attack ethereal enemies.

Ether spiders are not mindless or cruel—they are simply hungry. If a prospective meal can sate an ether spider's incredible appetite through other means, they might be able to bargain for their life. Ether spiders are especially interested in items, information, or allies who can help them against their enemies.

Ether spiders dwell in vast nests adrift in the Ethereal Plane, where as many as half a dozen ether spiders might cohabitate. Although ether spiders enjoy one another's company, they don't form the same bonds as most humanoids, and they are more likely to feast on the corpse of a fallen sibling than save one from certain doom. When not hunting prey, ether spiders are likely to let down their guard. Travelers who find a floating ether spider commune should have an easier time of making peaceful contact to trade with or even befriend these strange arachnids. The nests drift on metaphysical currents and are rarely seen in the same vicinity twice.

Sometimes a point of interest in the neighboring Universe compels them to tether their nest to an area, creating a semipermanent home.

```statblock
creature: "Ether Spider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
