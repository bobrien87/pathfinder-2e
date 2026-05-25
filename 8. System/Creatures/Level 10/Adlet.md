---
type: creature
group: ["Cold", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Adlet"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Cold"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Adlet, Common"
skills:
  - name: Skills
    desc: "Acrobatics +20, Athletics +21, Stealth +20, Survival +18"
abilityMods: ["+5", "+6", "+4", "+0", "+4", "+0"]
abilities_top:
  - name: "Frozen Weapons"
    desc: "Weapons wielded by an adlet gain the effect of the [[Frost]] property rune."
  - name: "Pack Attack"
    desc: "An adlet's Strikes deal an additional 2d6 damage to creatures that are within the reach of at least two of the adlet's allies."
armorclass:
  - name: AC
    desc: "29; **Fort** +20, **Ref** +22, **Will** +16"
health:
  - name: HP
    desc: "180; **Immunities** cold; **Weaknesses** fire 10"
abilities_mid:
  - name: "Avenging Bite"
    desc: "`pf2:r` **Trigger** A creature within reach of an adlet's jaws Strike attacks one of the adlet's allies. <br>  <br> **Effect** The adlet makes a jaws Strike against the triggering creature."
  - name: "Wolfstorm"
    desc: "60 feet. A clammy, frigid mist billows forth ahead of the adlet. Creatures within the mist become [[Concealed]], and creatures outside the mist become concealed to creatures within it. An adlet can see through the aura without penalty."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +20 (`pf2:1`) (magical), **Damage** 2d6+9 piercing"
  - name: "Melee strike"
    desc: "Jaws +19 (`pf2:1`) (unarmed), **Damage** 2d8+9 slashing plus 1d6 cold"
  - name: "Melee strike"
    desc: "Spear +21 (`pf2:1`) (magical, thrown 20), **Damage** 2d6+9 piercing"
spellcasting: []
abilities_bot:
  - name: "Wolfrime"
    desc: "`pf2:1` An adlet's mist turns biting cold and coalesces into a thick rime of frost that deals 6d6 cold damage to creatures inside the adlet's wolfstorm aura (DC 26 [[Fortitude]] save), and the aura is deactivated until the start of the adlet's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Adlets dwell in the farthest, harshest reaches of the Crown of the World, with a few journeying beyond to similarly frigid regions in other continents. At frst glance, these isolated people look much like their Erutaki human cousins; they typically have straight, black hair and compact, powerful builds. However, adlets tend move with more grace their human kin. Up close, their strangeness reveals itself, as each has a furry face and sports a maw full of wolfike teeth. Their legs and tails resemble those of dogs.

Adlets' legends say that long ago, a mighty hunter lost his way far from home and came upon a house of whalebone and ice. A woman dressed in white fox furs greeted him, fed him, and tended to his frostbite. In time, they married and had 10 children, fve of whom bore the legs and tails of foxes. These children stayed with their mother, while the other fve—born with the legs and tails of wolves—traveled with their father back to the human lands and became the frst adlets.

Most adlets aren't inherently evil, but their culture is warlike, xenophobic, and noticeably lacking in humility. They see themselves as the natural rulers of the arctic wastes and view everyone else as squatters at best and invaders at worst. A typical adlet is stronger and faster than any mundane human, with the ability to walk naked in a blizzard and call up ice-cold mists. Given that, it's little wonder that adlets have developed something of a superiority complex. Still, while adlet raids are a common problem for travelers in the Crown of the World, a handful of wily and intrepid merchants have forged peaceful relations with certain adlet communities along more common routes.

```statblock
creature: "Adlet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
