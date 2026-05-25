---
type: creature
group: ["Darvakka", "Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vanyver"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Greater Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Common, Diabolic, Necril (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +23, Arcana +23, Athletics +27, Religion +24, Stealth +25, Netherworld Lore +25, Void Lore +25"
abilityMods: ["+8", "+4", "+6", "+4", "+5", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "34; **Fort** +29, **Ref** +23, **Will** +22"
health:
  - name: HP
    desc: "275; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** holy 10, silver 10; **Resistances** cold 10"
abilities_mid:
  - name: "Catching Bite"
    desc: "`pf2:r` **Trigger** A creature within reach of the vanyver's jaws makes a melee Strike against the vanyver with a weapon <br>  <br> **Effect** The vanyver chooses to be hit. If the attack would've missed, it hits. The vanyver catches the weapon in their jaws and uses Drain Magic on it without fulfilling Drain Magic's requirements."
  - name: "Drain Magic"
    desc: "`pf2:1` **Requirements** The vanyver's last action was a successful jaws Strike against a creature, object, or spell effect <br>  <br> **Effect** The vanyver casts an innate [[Dispel Magic]] on the same target; if the target was a creature, the vanyver can target a spell affecting the creature instead. If a spell effect or item is successfully counteracted, the vanyver gains temporary Hit Points equal to double the counteract rank of the effect that was counteracted."
  - name: "Entropy's Shadow"
    desc: "40 feet. Vanyvers leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 3d6 void damage with a DC 30 [[Fortitude]] save. If it fails, it's also [[Enfeebled]] 1 for 1 minute and pulled 10 feet toward the vanyver."
  - name: "Snatch"
    desc: "The vanyver can Fly at half Speed while they have a creature [[Grabbed]] or [[Restrained]] in either or both of their talons, carrying that creature along with them."
  - name: "Sunlight Powerlessness"
    desc: "A vanyver caught in sunlight is [[Stunned]] 2 and [[Clumsy]] 2."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Talon +27 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d10+11 bludgeoning plus 1d10 cold plus [[Grab]]"
  - name: "Melee strike"
    desc: "Wing +27 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 3d6+11 bludgeoning plus 1d10 cold"
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d10+11 piercing plus 1d10 cold plus [[Drain Magic]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26<br>**7th** [[Interplanar Teleport (to the Universe, Void, or Netherworld only)]]<br>**2nd** [[Darkness]], [[Dispel Magic]] (At Will), [[See the Unseen]]<br>**1st** [[Detect Magic]], [[Harm]]"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(3d10+5)[piercing]] DC 33 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Vanyvers are large, humanoid bats shaped from void and shadowstuff, their red eyes glowing like tiny stars in an otherwise lightless night. Though powerful, they're the least of the darvakkas, and the most likely to submit to a master, either another of their kind or a mortal with a reputation for being especially murderous and destructive. Vanyvers agree to follow their masters as a temporary means of maximizing the death and destruction they can enact but will quickly turn on any master they feel falters in this goal.

Darvakkas, also called nightshades, are a ravenous evil made up of equal parts darkness and malice. Originally creatures of the Outer Planes who travel to the convergence of the Shadow Plane and the Void—where the power of nothingness obliterates them—these undead abominations are the physical embodiment of entropy. They burn with an intense hatred for all life, working to bring a final, dark night to the Material Plane where nothing but ash and ice remain.

As creatures twisted by darkness and shadow, darvakkas have a great aversion to sunlight and all sources of vitality energy. On the Material Plane, they spend the hours of daylight hidden below ground, amid ruins, or submerged deep in the ocean's darkest chasms beyond the reach of the sun's rays, emerging when darkness shelters them overhead.

Darvakkas have an aura of entropy that attracts undead thralls to serve as warriors and heralds. They rarely seek alliances with each other or other creatures, existing in solitude as the heads of individual armies of the dead.

```statblock
creature: "Vanyver"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
