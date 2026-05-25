---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hyakume"
level: "15"
rare_01: "Uncommon"
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
    desc: "+29; [[Darkvision]]"
languages: "Aklo, Common (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +30, Crafting +30, Deception +27, Medicine +25, Nature +25, Occultism +30, Religion +27, Society +28, Thievery +25, Bardic Lore +28"
abilityMods: ["+4", "+6", "+4", "+9", "+6", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Lore Master"
    desc: "A hyakume can use their Bardic Lore skill to Recall Knowledge on any topic, and they know any languages common to an area they have spent a day or more in."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Scatterbrain Palm"
    desc: "A creature hit by the hyakume's fist Strike must attempt a DC 36 [[Will]] save. The creature is then temporarily immune until start of its next turn. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Stunned]] 1. <br> - **Failure** The creature is [[Stunned]] 2. <br> - **Critical Failure** The creature is [[Stunned]] 3 and the hyakume can use [[Steal]] Memories on the target as part of this action."
armorclass:
  - name: AC
    desc: "36 all-around vision; **Fort** +23, **Ref** +25, **Will** +29"
health:
  - name: HP
    desc: "275; **Immunities** confused; **Resistances** mental 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+2 Status to All Saves vs. Magic"
    desc: ""
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +27 (`pf2:1`) (agile, finesse, magical, reach 10 ft.), **Damage** 3d10+10 bludgeoning plus [[Scatterbrain Palm]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 40, attack +32<br>**8th** [[Disappearance]], [[Hidden Mind]]<br>**4th** [[Fly]] (At Will)<br>**3rd** [[Hypercognition]] (At Will), [[Ring of Truth]] (At Will)<br>**2nd** [[Dispel Magic]]<br>**1st** [[Charm]], [[Daze]], [[Detect Magic]], [[Mindlink]] (At Will), [[Read Aura]]"
abilities_bot:
  - name: "Eye Probe"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Effect** Up to six of the hyakume's eyes detach from the hyakume's body. Each eye has AC 26, HP 1, and a fly speed of 40 feet. <br>  <br> The hyakume can see through all of their eye probes. They can move the probes all in separate directions using a single Sustain action. <br>  <br> A hyakume can have no more than six eye probes active at a time; using this ability to create more causes the eye or eyes farthest away to shrivel and die. <br>  <br> The hyakume can deliver touch spells through their eye probes and can make melee spell attacks through them. In addition, the hyakume can Steal Memories through an eye probe using a single action by touching the target with the eye."
  - name: "Steal Memories"
    desc: "`pf2:3` The hyakume reaches out with their mind and attempts to steal memories from a creature within 30 feet. <br>  <br> The target must succeed at a DC 40 [[Will]] save saving throw or become [[Stupefied 2]] and have some of its memories stolen. The hyakume learns some of the target's memories (chosen by the GM), which are then lost to the target."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Hundreds of bloodshot eyes peek out from under the fleshy layers of a hyakume's skin. These hulking aberrations covet knowledge and go to great lengths to keep what they know to themselves; they'll destroy scriptoria they've raided and burn books they've read to ensure no other soul learns their contents. While hyakume occasionally trade valuable information to garner greater knowledge, they're liable to trick their targets into revealing more than they should. Most frightening of all is the hyakume's ability to steal memories and erase any knowledge of their existence from the minds of their victims.

```statblock
creature: "Hyakume"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
