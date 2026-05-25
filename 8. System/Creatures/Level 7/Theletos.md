---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Theletos"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "envisioning"
skills:
  - name: Skills
    desc: "Arcana +16, Intimidation +16, Religion +18, Stealth +15"
abilityMods: ["+4", "+4", "+3", "+3", "+5", "+3"]
abilities_top:
  - name: "Envisioning"
    desc: "When a theletos conveys information, it does so wordlessly through psychic projections. This acts as [[Telepathy]] with a range of 100 feet but is understandable to all creatures regardless of whether they have a language. The meaning to non-aeons can be vague and is often mysterious. A theletos can use this ability to communicate flawlessly with any other aeon on the same plane."
  - name: "Fate Drain"
    desc: "A creature damaged by the theletos's tentacle must succeed at a DC 22 [[Will]] save or become [[Stupefied 1]]. <br>  <br> As long as the creature is stupefied, it can no longer benefit from fortune effects. If the target fails additional saves against this ability, the condition value increases by 1 (to a maximum of stupefied 4). This condition value decreases by 1 every 24 hours."
armorclass:
  - name: AC
    desc: "25; **Fort** +16, **Ref** +13, **Will** +18"
health:
  - name: HP
    desc: "125; **Weaknesses** spirit 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (magical, unarmed), **Damage** 2d10+8 bludgeoning"
  - name: "Melee strike"
    desc: "Tentacle +17 (`pf2:1`) (agile, magical, unarmed), **Damage** 2d8+8 slashing plus [[Fate Drain]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Outcast's Curse]], [[Suggestion]]<br>**3rd** [[Enthrall]]<br>**2nd** [[Augury (At will)]], [[Cleanse Affliction]], [[Dispel Magic]], [[Stupefy]]<br>**1st** [[Charm]]"
abilities_bot:
  - name: "Wrath of Fate"
    desc: "`pf2:2` The theletos releases a @Template[cone|distance:60] of energy from its center. Creatures in the cone become overwhelmed with the knowledge of various fates that destiny has in store for them and lack of clear pathways to these potential futures. They must succeed at a DC 26 [[Will]] save or be [[Slowed]] 1 indefinitely. <br>  <br> An affected creature can choose to roll twice when it attempts an attack, saving throw, or skill check and take the lower result. Regardless of the outcome, that creature is no longer slowed after that roll. <br>  <br> > [!danger] Effect: Wrath of Fate <br>  <br> The theletos can't use Wrath of Fate again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Theletoses maintain the balance between fate and free will. A theletos is a roughly spherical mass of crystals from which emerge four limbs, each split at the elbow and ending in three-fngered hands. A pair of crystalline tentacles also emerges from its body. Those who have been damaged by a theletos's tentacles describe being presented with a disorienting dilemma: they feel forced to make a single choice while simultaneously being overwhelmed by the endless options available to choose from. Theletoses are more likely than most aeons to interfere in non-aeon societies, particularly in regions with draconian laws. Their involvement is twofold; a theletos concerns itself with both the freedom of individuals and the laws that restrict these individuals, even (or especially) when the two are in opposition.

```statblock
creature: "Theletos"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
