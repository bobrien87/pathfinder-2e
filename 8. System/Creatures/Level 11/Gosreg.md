---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gosreg"
level: "11"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]], [[Thoughtsense]] (precise) 60 feet"
languages: "Aklo, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Deception +24, Diplomacy +22, Occultism +23, Society +19, Stealth +23"
abilityMods: ["+3", "+6", "+3", "+6", "+5", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Borrow Languages"
    desc: "The gosreg can read and speak all languages known by creatures within range of its telepathy."
  - name: "Thoughtsense 60 feet"
    desc: "The gosreg senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
armorclass:
  - name: AC
    desc: "31; **Fort** +18, **Ref** +23, **Will** +22"
health:
  - name: HP
    desc: "195; **Immunities** confused; **Resistances** mental 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Unsettled Aura"
    desc: "30 feet. <br>  <br> Gosregs project a field of discordant energy that unsettles the minds of thinking creatures. Any non-mindless creature within 30 feet of a gosreg takes a –1 status penalty to Will saves. <br>  <br> > [!danger] Effect: Unsettled Aura"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (finesse, unarmed), **Damage** 2d10+7 piercing plus 1d10 mental"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d8+7 slashing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +22<br>**6th** [[Phantasmal Calamity]]<br>**5th** [[Mind Probe]], [[Sending]], [[Subconscious Suggestion]], [[Synaptic Pulse]]<br>**4th** [[Nightmare]], [[Suggestion]]<br>**1st** [[Phantom Pain]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Broadcast Stance"
    desc: "`pf2:1` **Requirements** the gosreg is in its natural form <br>  <br> **Effect** The gosreg secures its limbs into the ground as its brain-like head crackles with psychic energy. The gosreg's unsettled aura extends to 60 feet, and it blocks all other creatures' telepathy in the aura. Its Mind Bolt can also affect any number of targets in 60 feet. These effects end when the gosreg uses its claw Strike, leaves its space, or is knocked [[Prone]]."
  - name: "Change Shape"
    desc: "`pf2:1` The gosreg takes on the appearance of any Small or Medium humanoid. This doesn't change its Speed or attack and damage modifiers with its claw, but it might change the damage type it deals (typically to bludgeoning). It cannot use its jaws Strike while in humanoid form. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Mind Bolt"
    desc: "`pf2:2` A gosreg concentrates its field of discordant mental energy and projects it into the mind of one creature within 60 feet. The target takes 6d6 mental damage (DC 30 [[Will]] save). On a critical failure, the creature is also [[Confused]] for 1 minute or until it takes damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gosregs are agents of the Dominion of the Black who insinuate themselves into humanoid societies to implement the goals of their sinister masters. They're generally tasked with observing and waiting, hiding in disguised forms until their location is ripe for harvest. When this occurs, they reveal themselves as living psychic beacons, signaling their distant masters and guiding invasion forces. Over the years of an infiltration, a gosreg will assume dozens of roles, relishing any intense emotions it can inspire while laying the groundwork for future identities.

In their natural form, gosregs dart about in a jerky gallop due to stumpy legs, gangly arms, and oversized heads. They take on the appearances of humanoids to infiltrate societies, and they drop these disguises only when they're compromised and must resort to physical violence to continue their mission.

The Dominion of the Black is a conglomeration of deep-space conquerors with a strong presence on Aucturn, the most remote planet in Golarion's solar system. The Dominion has secret outposts all over Golarion; most of its members on the planet are scouts, using their skills to steal brains and identities, gathering information without any consideration for the inhabitants of the worlds they infiltrate.

```statblock
creature: "Gosreg"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
