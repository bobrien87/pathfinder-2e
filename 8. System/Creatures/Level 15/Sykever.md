---
type: creature
group: ["Darvakka", "Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sykever"
level: "15"
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
    desc: "+29; [[Greater Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Common, Diabolic, Necril (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +27, Athletics +29, Intimidation +28, Religion +27, Stealth +27, Netherworld Lore +27, Void Lore +27, Warfare Lore +27"
abilityMods: ["+8", "+4", "+6", "+6", "+6", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "37; **Fort** +25, **Ref** +25, **Will** +31"
health:
  - name: HP
    desc: "335; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** holy 10, silver 10; **Resistances** cold 10"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "40 feet. Sykevers leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 4d6 void damage with a DC 33 [[Fortitude]] save. If it fails, it's also [[Enfeebled]] 1 for 1 minute and pulled 10 feet toward the sykever."
  - name: "Sunlight Powerlessness"
    desc: "A sykever caught in sunlight is [[Stunned]] 2 and [[Clumsy]] 2."
  - name: "Crush Item"
    desc: "`pf2:r` **Trigger** The sykever gets a critical success to [[Disarm]] <br>  <br> **Requirements** The sykever is in their bipedal stance <br>  <br> **Effect** The sykever snatches the item and pierces it with their arm spikes. The item becomes broken and falls to the ground in the sykever's space. Items that are already broken aren't further damaged, and an item with 14 or higher Hardness is unaffected."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +31 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d8+12 bludgeoning plus 1d10 cold plus 2d8 bleed"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28<br>**7th** [[Interplanar Teleport (to the Universe, Void, or Netherworld only)]]<br>**6th** [[Truesight]]<br>**4th** [[Fly]] (Constant)<br>**3rd** [[Paralyze]]<br>**2nd** [[Darkness]] (At Will), [[Invisibility]]<br>**1st** [[Detect Magic]], [[Harm]]"
abilities_bot:
  - name: "Change Posture"
    desc: "`pf2:1` The sykever changes between their bipedal and quadrupedal stance. In their bipedal stance, the sykever can use all the abilities in their stat block except Horned Rush. In their quadrupedal stance, the sykever has a Speed of 80 feet but can't make arm spike Strikes, Disarm, cast spells, or use Crush Item."
  - name: "Draining Gaze"
    desc: "`pf2:1` The sykever fixes their nightmarish gaze on one creature they can see, who must attempt a DC 36 [[Will]] save. Regardless of the result, the target is temporarily immune for 10 minutes. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Enfeebled]] 2 for 1 round if the sykever is in bipedal stance, or [[Clumsy]] 2 for 1 round if the sykever is in quadrupedal stance. <br> - **Failure** As success, but the effect lasts 1 minute. <br> - **Critical Failure** As success, but [[Enfeebled]] 3 or [[Clumsy]] 3, and the effect lasts 10 minutes."
  - name: "Horned Rush"
    desc: "`pf2:1` **Requirements** The sykever is in their quadrupedal stance <br>  <br> **Effect** The sykever Strides and then makes a horn Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The most common darvakkas are sykevers, walkers in the night. Bloodthirsty but calculating, they lead legions of dead into battle on the Material Plane, working toward the simple goal of ending all life.

Darvakkas, also called nightshades, are a ravenous evil made up of equal parts darkness and malice. Originally creatures of the Outer Planes who travel to the convergence of the Shadow Plane and the Void—where the power of nothingness obliterates them—these undead abominations are the physical embodiment of entropy. They burn with an intense hatred for all life, working to bring a final, dark night to the Material Plane where nothing but ash and ice remain.

As creatures twisted by darkness and shadow, darvakkas have a great aversion to sunlight and all sources of vitality energy. On the Material Plane, they spend the hours of daylight hidden below ground, amid ruins, or submerged deep in the ocean's darkest chasms beyond the reach of the sun's rays, emerging when darkness shelters them overhead.

Darvakkas have an aura of entropy that attracts undead thralls to serve as warriors and heralds. They rarely seek alliances with each other or other creatures, existing in solitude as the heads of individual armies of the dead.

```statblock
creature: "Sykever"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
