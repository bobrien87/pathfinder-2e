---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sportlebore Swarm"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +17, Stealth +17"
abilityMods: ["+2", "+6", "+4", "-4", "+2", "+4"]
abilities_top:
  - name: "Sportlebore Infestation"
    desc: "**Saving Throw** DC 22 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 1 (1 hour) <br>  <br> **Stage 3** [[Enfeebled]] 2 (1 hour) <br>  <br> **Stage 4** 4d6 bludgeoning damage (DC 25 [[Fortitude]] save) as the host painfully vomits out a sportlebore swarm and returns to stage 1"
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +17, **Will** +13"
health:
  - name: HP
    desc: "85; **Immunities** precision, swarm mind; **Weaknesses** area damage 7, splash damage 7; **Resistances** bludgeoning 3, piercing 7, slashing 7"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
  - name: "Pour Down Throat"
    desc: "`pf2:r` **Trigger** A creature in the sportlebore swarm's area speaks, Casts a Spell, or opens its mouth <br>  <br> **Effect** A portion of the sportlebore swarm attempts to surge down the throat of the triggering creature, who must attempt a DC 25 [[Fortitude]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature gets a mouthful of sportlebores. They spit the insects out and avoid further damage, but they can't speak for 1 round, and if they were performing a spellcasting action, the spell fails and the caster wastes the action. <br> - **Failure** The creature takes 4d6 piercing damage from sportlebore bites, can't speak for 1 round, and loses a spell as noted under success. <br> - **Critical Failure** As failure, but the creature is also exposed to sportlebore infestation."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each creature in the sportlebore swarm's area takes @Damage[3d6[piercing]|options:area-damage] damage (DC 25 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A swarm of sportlebores is a much more dangerous foe than a single insect.

The bane of hungry adventurers the world over, sportlebores are nefarious vermin that resemble delicious snacks. When positioned near trail rations, such as fruit or jerky, a sportlebore can flawlessly imitate these foodstuffs by flexing, contorting, and color-shifting its abdomen, then folding its thorax, head, and legs within its delicious-looking body. Once consumed, the sportlebore reproduces into a hungry swarm that's regurgitated by the now ailing eater, ravenously attacking any creatures it thinks it can consume.

```statblock
creature: "Sportlebore Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
