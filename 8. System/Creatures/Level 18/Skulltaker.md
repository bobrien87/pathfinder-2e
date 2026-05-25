---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skulltaker"
level: "18"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+33; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Necril (Skeletal Lore languages)"
skills:
  - name: Skills
    desc: "Acrobatics +34, Intimidation +35, Religion +30, Stealth +32, Skeletal Lore +30"
abilityMods: ["+8", "+6", "+6", "+2", "+8", "+7"]
abilities_top:
  - name: "Skeletal Lore"
    desc: "A skulltaker taps into the memories of the creatures whose bones make up its body. This gives it the Skeletal Lore skill, which it can use to Recall Knowledge of any kind. In addition, it can speak and understand all the languages known by the creatures whose bones make up its body (typically including Common and the regional language of the skulltaker's home region). <br>  <br> The skulltaker can use Skeletal Lore as the primary skill check for the [[Collective Memories]] ritual, and it can cast *collective memories* without secondary casters."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Bonetaker"
    desc: "Whenever a creature dies within 60 feet of a skulltaker, the skulltaker draws a portion of the creature's bones into its shard storm. <br>  <br> The creature must succeed at a DC 40 [[Will]] save or rise as a [[Skeletal Champion]] in 1d4 rounds. These skeletal champions are controlled by the skulltaker."
  - name: "Vitality Drain"
    desc: "When a skulltaker hits with a melee Strike, the target must succeed at a DC 40 [[Fortitude]] save or become [[Drained]] 2 and [[Doomed]] 1."
armorclass:
  - name: AC
    desc: "42; **Fort** +31, **Ref** +33, **Will** +35"
health:
  - name: HP
    desc: "300; void healing; **Immunities** cold, death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** piercing 15, slashing 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Vitality"
    desc: ""
  - name: "Shard Storm"
    desc: "10 feet. <br>  <br> A cloud of bone shards surrounds the skulltaker. When a creature moves into the emanation or begins its turn there, shard storm deals @Damage[4d6[slashing],4d6[void]]{4d6 slashing damage and 4d6 void damage} to the creature, with a DC 40 [[Reflex]] save. <br>  <br> If the creature has resistance or immunity to void damage, or an effect that protects it against death effects, or an effect that protects it against the doomed or drained condition, the creature must first succeed at a DC 40 [[Will]] save or have all such benefits suppressed for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +35 (`pf2:1`) (deadly 2d12, magical, reach 10 ft., unarmed), **Damage** 3d10+14 piercing plus 3d6 void plus [[Energy Drain]]"
  - name: "Melee strike"
    desc: "Claw +35 (`pf2:1`) (agile, deadly 2d12, magical, reach 15 ft., unarmed), **Damage** 3d6+14 slashing plus 3d6 void plus [[Energy Drain]]"
  - name: "Melee strike"
    desc: "Bone Javelin +33 (`pf2:1`) (magical, thrown 100), **Damage** 3d8+6 piercing plus 3d6 void"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40, attack +32<br>**8th** [[Desiccate]], [[Punishing Winds]]<br>**7th** [[Execute]]<br>**6th** [[Truesight]] (Constant)"
abilities_bot:
  - name: "Splintered Ground"
    desc: "`pf2:1` The skulltaker causes splintered bones to erupt from all solid surfaces in a @Template[emanation|distance:100], except for surfaces of worked stone. A creature moving through the bones takes @Damage[10[piercing],10[void]|options:area-damage]{10 piercing damage and 10 void damage} for every 5 feet of movement. <br>  <br> The first time each round a creature takes piercing damage from these splintered bones, it must succeed at a DC 40 [[Reflex]] save or take a –10-foot circumstance penalty to all Speeds for 10 minutes, or a –15-foot circumstance penalty for 24 hours on a critical failure. <br>  <br> The bones remain in place until the skulltaker uses this action again or the bones are manually removed, which takes 10 minutes for each 5-foot square. <br>  <br> > [!danger] Effect: Splintered Ground <br>  <br> > [!danger] Effect: Splintered Ground (Critical Failure)"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Swirling down from misty peaks and through howling mountain passes like an evil wind, the vortex of bones known as a skulltaker is a terrible manifestation of the delirium and agony experienced by doomed climbers and lost trailblazers just before they met their end. In some places, a skulltaker is also known as a saxra.

```statblock
creature: "Skulltaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
