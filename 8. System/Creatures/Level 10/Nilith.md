---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nilith"
level: "10"
rare_01: "Common"
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
    desc: "+19; [[Darkvision]]"
languages: "Aklo, Common (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +17, Intimidation +23, Occultism +19, Stealth +21, Survival +17"
abilityMods: ["+3", "+5", "+4", "+3", "+3", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "32; **Fort** +17, **Ref** +20, **Will** +20"
health:
  - name: HP
    desc: "150; **Resistances** mental 10, physical 5 except silver"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 2d10+9 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Fangs +23 (`pf2:1`) (finesse, magical), **Damage** 2d12+9 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Hallucination]], [[Mind Probe]], [[Wave of Despair]]<br>**4th** [[Confusion]], [[Flicker]], [[Nightmare]]<br>**3rd** [[Dream Message]], [[Mind Reading]] (At Will)<br>**2nd** [[Invisibility (At Will, Self Only)]]<br>**1st** [[Message]], [[Read Aura]], [[Shield]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Mind Crush"
    desc: "`pf2:1` **Requirements** The nilith has a creature [[Grabbed]] <br>  <br> **Effect** The nilith reaches into the mind of the grabbed creature and implants disjointed images of the victim's worst fears and nightmares. The grabbed creature takes 6d6 mental damage with a DC 31 [[Will]] save. On a critical failure, the target is also affected as though by [[Never Mind]], and it must attempt a second Will save against that effect."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The sleek, dark niliths resemble hairless, emaciated tree sloths. These creatures are intensely dangerous and fearsome, with glowing red eyes, wicked claws, and mouths full of needlelike teeth. Niliths feed off the emotions, fears, and flesh of the living, and folktales posit that those who have nightmares of these creatures are fated to one day be eaten by them. Niliths draw intense joy from tormenting sapient creatures, often focusing their predations on the pious and the just, from whom they draw forth their most basic fears and worst thoughts and revel in their victims' subsequent terror. More often than not, these despicable manipulators wish to drive their victims into madness and even to suicide. Most niliths lack the patience to spend too much time fully tearing down an individual, and when a nilith tires of its current plaything and becomes bored with its particular thoughts and fears, it murders the quarry before feeding on its flesh and moving onto the next victim.

Niliths are actually extensions of much deadlier creatures that dwell in a distant dimension beyond dreams—in a way, niliths are little more than remote feeding machines for the unknown alien entities to which they are connected. Scholars and dimensional travelers have attempted to uncover the exact mechanisms of this mysterious connection, but they have yet to decipher the truth. Indeed, many who investigate the nature of a nilith's bond are driven to madness before getting anywhere close. The odd connection to otherworldly beings might help explain the longevity of these creatures, as it is believed that niliths can live for thousands of years.

Thankfully for others, niliths are solitary creatures that hate the company of their own kind, likely because these harbingers of nightmares have no wish to taste the horrors they bring to others.

```statblock
creature: "Nilith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
