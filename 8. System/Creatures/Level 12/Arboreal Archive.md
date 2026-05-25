---
type: creature
group: ["Plant", "Wood"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Arboreal Archive"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Plant"
trait_02: "Wood"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Low-Light Vision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Arboreal, Common, Fey (speak with plants)"
skills:
  - name: Skills
    desc: "Athletics +23, Diplomacy +22, Nature +25, Stealth +19, Forest Lore (applies to the arboreal archive's territory) +28"
abilityMods: ["+7", "-1", "+5", "+4", "+7", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +17, **Will** +27"
health:
  - name: HP
    desc: "230; **Weaknesses** axe vulnerability 10, fire 15; **Resistances** bludgeoning 10, piercing 10"
abilities_mid:
  - name: "Abeyance Rift"
    desc: "If an arboreal archive dies unexpectedly before passing on their knowledge in a succession ritual, the amassed lore within their roots and boughs explodes out in a shock wave that deals @Damage[8d10[mental]|options:area-damage,inflicts:prone] damage to creatures within @Template[emanation|distance:30]{30 feet} (DC 32 [[Will]] save) before dissipating; those who fail also fall [[Prone]]."
  - name: "Axe Vulnerability"
    desc: "An arboreal archive takes 10 additional damage from axes."
  - name: "Improved Knockdown"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature as a free action. This attempt neither applies nor counts toward the monster's multiple attack penalty."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Branch +25 (`pf2:1`) (reach 15 ft.), **Damage** 3d10+10 bludgeoning plus [[Improved Knockdown]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 32, attack +24<br>**6th** [[Tangling Creepers]]<br>**3rd** [[Earthbind]] (At Will), [[Speak with Plants]] (Constant)<br>**2nd** [[Entangling Flora]]"
abilities_bot:
  - name: "Memory Maelstrom"
    desc: "`pf2:3` The arboreal archive tries to overwhelm foes with a surge of information it has absorbed over its long life. This surge deals @Damage[5d6[mental]|options:area-damage] damage to each enemy within @Template[emanation|distance:40]{40 feet}, who must attempt a DC 32 [[Will]] save. <br> - **Critical Success** The creature maintains its composure, takes no damage, and is temporarily immune to Memory Maelstrom for 1 minute. <br> - **Success** The creature is [[Stunned]] 1 and takes half damage. <br> - **Failure** The creature takes full damage and is [[Stunned]] 3. <br> - **Critical Failure** The creature takes double damage, is [[Confused]] for 2d4 rounds, and is stunned 3."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Arboreal archives are solitary beings typically found in the remote wilderness. These ancient monoliths hold the memories of their vast territories, keeping mental records of the passing seasons of the world around them. Their knowledge of humanoid affairs varies, as they find quickly shifting political situations difficult to comprehend, but through fungal networks, reports from arboreal wardens, and other woodland chatter, arboreal archives learn of each storm, drought, or logging threat encountered throughout their long years. They primarily observe and record rather than interfere, but they willingly offer wisdom to those who respectfully seek them out. Arboreal regents call upon archives for advice in times of strife, conferring on the best course of action to protect their realms.

It is rare for there to be more than one arboreal archive in a given region. When an archive senses they're nearing the end of their lengthy lifespan, a grove of regents gathers to nominate the wisest among them to become the next archive. After four seasons' deliberation, all arboreals in the area congregate to witness the succession ritual, during which the elder arboreal archive transfers their collected wisdom to the elected replacement before retiring.

Arboreals are tree-like ancient guardians of forests, nurturing new growth and maintaining a balanced ecosystem as if the vast wilderness were their garden. Arboreals are thoughtful and deliberate - until something threatens their realms and invites their wrath.

```statblock
creature: "Arboreal Archive"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
