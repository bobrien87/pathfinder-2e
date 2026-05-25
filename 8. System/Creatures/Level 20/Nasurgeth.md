---
type: creature
group: ["Aquatic", "Darvakka"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nasurgeth"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Darvakka"
trait_03: "Shadow"
trait_04: "Undead"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Greater Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Common, Diabolic, Necril (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +36, Athletics +39, Religion +36, Stealth +34, Shadow Plane Lore +36, The Void Lore +36"
abilityMods: ["+11", "+6", "+7", "+8", "+8", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "45; **Fort** +35, **Ref** +32, **Will** +36"
health:
  - name: HP
    desc: "510; void healing; **Immunities** cold, death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** holy 15, silver 15"
abilities_mid:
  - name: "Midnight Depths"
    desc: "60 feet. A nasurgeth's entropy grows even stronger underwater. All water within the aura is completely dark (as 4th-rank [[Darkness]]). Magical light with a counteract rank of 4th level or lower, along with magical light cantrips, are suppressed. A living creature entering or starting its turn in the aura takes @Damage[4d6[void]|options:area-damage] damage, and the creature also takes an additional 2d10 cold damage if it's in water (DC 39 [[Fortitude]] save). If it fails, it's also [[Enfeebled]] 1 for 1 minute and pulled 10 feet toward the nasurgeth."
  - name: "Spray Black Bile"
    desc: "`pf2:r` **Trigger** The nasurgeth takes slashing or piercing damage from a critical hit, or a swallowed creature cuts itself free <br>  <br> **Effect** Darkness and void energy spill out from the nasurgeth's wound, dealing 8d8 void damage to creatures within 20 feet (DC 40 [[Fortitude]] save)."
  - name: "Sunlight Powerlessness"
    desc: "A nasurgeth caught in sunlight is [[Stunned]] 2 and [[Clumsy]] 2."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +39 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 3d10+19 piercing plus 2d10 cold plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Tail +39 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 3d6+19 bludgeoning plus 2d10 cold"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 43, attack +35<br>**7th** [[Eclipse Burst]], [[Interplanar Teleport (to the Universe, Void, or Netherworld only)]]<br>**6th** [[Truesight]]<br>**1st** [[Detect Magic]], [[Harm]]"
abilities_bot:
  - name: "Broken Barb"
    desc: "`pf2:1` **Requirements** A creature is [[Grabbed]] or [[Restrained]] in the nasurgeth's jaws <br>  <br> **Effect** The nasurgeth breaks a tooth off in the target, who takes 3d10 bleed and is no longer grabbed or restrained. If the target is adjacent to a surface, the tooth also pins it in place, making it [[Immobilized]] (`act escape dc=45`)."
  - name: "Ravenous Void"
    desc: "`pf2:3` The nasurgeth barrels forward with their mouth open, Swimming twice in a straight line and moving through the spaces of Huge or smaller creatures. The nasurgeth deals the damage of their jaws Strike to each creature whose space they enter (DC 45 [[Reflex]] save). Any creature that critically fails is automatically Swallowed Whole."
  - name: "Swallow Whole"
    desc: "`pf2:1` Huge, @Damage[(2d10+9)[bludgeoning]], Rupture 40 <br>  <br> A living creature that ends its turn swallowed whole by a nasurgeth becomes [[Drained]] 1 or increases its drained condition by 1, and the nasurgeth gains 20 temporary Hit Points. A creature whose drained condition increases to 5 in this way dies. <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Nasurgeths are hungry voids with glowing eyestalks and thousands of teeth. They lurk deep beneath the waves where the sunlight doesn't reach. At night, they ascend to the skies and rain destruction and ruin down on all the living.

Darvakkas, also called nightshades, are a ravenous evil made up of equal parts darkness and malice. Originally creatures of the Outer Planes who travel to the convergence of the Shadow Plane and the Void—where the power of nothingness obliterates them—these undead abominations are the physical embodiment of entropy. They burn with an intense hatred for all life, working to bring a final, dark night to the Material Plane where nothing but ash and ice remain.

As creatures twisted by darkness and shadow, darvakkas have a great aversion to sunlight and all sources of vitality energy. On the Material Plane, they spend the hours of daylight hidden below ground, amid ruins, or submerged deep in the ocean's darkest chasms beyond the reach of the sun's rays, emerging when darkness shelters them overhead.

Darvakkas have an aura of entropy that attracts undead thralls to serve as warriors and heralds. They rarely seek alliances with each other or other creatures, existing in solitude as the heads of individual armies of the dead.

```statblock
creature: "Nasurgeth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
