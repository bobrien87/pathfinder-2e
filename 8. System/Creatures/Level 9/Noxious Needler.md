---
type: creature
group: ["Alchemical", "Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Noxious Needler"
level: "9"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Alchemical"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +22"
abilityMods: ["+6", "+4", "+3", "-5", "+0", "-5"]
abilities_top:
  - name: "Alchemical Injection"
    desc: "When a noxious needler hits a creature with a syringe Strike, roll 1d6 on the alchemical chambers list to determine the additional effect of the attack. The syringe deals an additional 2d6 damage of the appropriate type (or exposes the target to the sickness effect, as appropriate). <br>  <br> `gmr 1d6 #Alchemical Injection`Alchemical Effect12d6 acid damage <br>  <br> 22d6 cold damage32d6 electricity damage42d6 fire damage52d6 poison damage6Sickness: DC 26 [[Fortitude]] save or [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)"
armorclass:
  - name: AC
    desc: "27; **Fort** +20, **Ref** +19, **Will** +15"
health:
  - name: HP
    desc: "150; **Resistances** physical 10 except adamantine, bludgeoning, spells 10 except sonic"
abilities_mid:
  - name: "Alchemical Chambers"
    desc: "A noxious needler's body contains six alchemical chambers filled with different substances. When a noxious needler's ability calls upon a randomly determined alchemical effect, roll 1d6 and consult the following (if you roll the result of a chamber that was shattered, there is no alchemical effect): <br>  <br> `gmr 1d6 #Alchemical Chambers`Alchemical Effect1Acid Damage <br>  <br> 2Cold Damage3Electricity Damage4Fire Damage5Poison Damage6Sickness: DC 26 [[Fortitude]] save or [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)"
  - name: "Alchemical Rupture"
    desc: "When a noxious needler takes physical damage from a critical hit or is affected by a shatter spell, one glass chamber within its body shatters, spewing alchemical liquid in a @Template[emanation|distance:5]. Roll on the alchemical chambers list to determine which one shatters—on a roll of 1–5, creatures in the area take 10d6 damage of the appropriate type (DC 28 basic Reflex). On a roll of 6, creatures must instead save against the sickness effect. <br>  <br> `gmr 1d6 #Alchemical Rupture`Alchemical Effect1@Damage[10d6[acid]|options:area-damage] damage DC 28 [[Reflex]] save <br>  <br> 2@Damage[10d6[cold]|options:area-damage] damage DC 28 [[Reflex]] save3@Damage[10d6[electricity]|options:area-damage] damage DC 28 [[Reflex]] save4@Damage[10d6[fire]|options:area-damage] damage DC 28 [[Reflex]] save5@Damage[10d6[poison]|options:area-damage] damage DC 28 [[Reflex]] save6Sickness: DC 26 [[Fortitude]] save or [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Syringe +22 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+6 piercing plus [[Alchemical Injection]]"
  - name: "Melee strike"
    desc: "Bomb +20 (`pf2:1`) (magical, thrown 20), **Damage**  plus [[Generate Bomb]]"
spellcasting: []
abilities_bot:
  - name: "Generate Bomb"
    desc: "`pf2:1` The needler fills an empty vial from one of its alchemical chambers to create a bomb and then makes a bomb Strike. Roll 1d6 on the table below. On a roll of 1–5, the bomb deals 3d10 damage and 3 splash damage, matching the damage type of the chamber; you can instead choose to create an alchemical bomb of 11th level or lower that deals the same damage type, such as an acid flask on a roll of 1. On a roll of 6, it creates a sickness bomb, which exposes the target and all creatures in the splash radius to the sickness effect; creatures hit by only the splash receive a +2 circumstance bonus to their Fortitude saves. <br>  <br> `gmr 1d6 #Generate Bomb` <br> Alchemical Effect <br>  <br> 1 <br>  <br> Acid Damage: @Damage[3d10[acid],(3[splash])[acid]] damage <br>  <br> 2 <br> Cold Damage: @Damage[3d10[cold],(3[splash])[cold]] damage <br>  <br> 3 <br> Electricity Damage: @Damage[3d10[electricity],(3[splash])[electricity]] damage <br>  <br> 4 <br> Fire Damage: @Damage[3d10[fire],(3[splash])[fire]] damage <br>  <br> 5 <br> Poison Damage: @Damage[3d10[poison],(3[splash])[poison]] damage <br>  <br> 6 <br> Sickness: DC 26 [[Fortitude]] save or [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This construct is a walking alchemical nightmare capable of inflicting all manner of painful wounds. The noxious needlers' ability to follow orders is granted by the otherwise mindless humanoid brain that floats in their dome-like heads, allowing them to serve as laborers and guards for their creators.

In exceptionally rare cases, the brain used in their creation might retain fragments of memories or even an actual intellect, resulting in a noxious needler with a personality and agenda of its own. Unwilling creations often hunt down their creators, venting their rage on similar targets if revenge is impossible. Others blankly replicate the experiments from their last memory

```statblock
creature: "Noxious Needler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
