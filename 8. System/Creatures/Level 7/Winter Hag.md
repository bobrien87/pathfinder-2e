---
type: creature
group: ["Cold", "Hag"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Winter Hag"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Cold"
trait_02: "Hag"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[See Invisibility]]"
languages: "Aklo, Common, Fey, Jotun"
skills:
  - name: Skills
    desc: "Athletics +13, Deception +17, Diplomacy +15, Occultism +15, Survival +14"
abilityMods: ["+4", "+2", "+3", "+4", "+3", "+6"]
abilities_top:
  - name: "Coven"
    desc: "A winter hag adds [[Howling Blizzard]], [[Rewrite Memory]], and [[Wall of Ice]] to their coven's spells <br>  <br> This monster can form a coven with two or more other creatures who also have the coven ability. This involves performing an 8-hour ceremony with all prospective coven members. After the coven is formed, each of its members gains elite adjustments, adjusting their levels accordingly. Coven members can sense other members' locations and conditions by spending a single action, which has the concentrate trait, and can sense what another coven member is sensing as a two-action activity, which has the concentrate trait as well. <br>  <br> Covens also grant spells and rituals to their members, but these can be cast only in cooperation between three coven members who are all within 30 feet of one another. A coven member can contribute to a coven spell with a single action that has the concentrate trait. If two coven members have contributed these actions within the last round, a third member can cast a coven spell on her turn by spending the normal spellcasting actions. A coven can cast its coven spells an unlimited number of times but can cast only one coven spell each round. All covens grant the 8th-rank [[Cursed Metamorphosis]] spell and all the following spells, which the coven can cast at any rank up to 5th: [[Augury]], [[Charm]], [[Clairaudience]], [[Clairvoyance]], [[Dream Message]], [[Illusory Disguise]], [[Illusory Scene]], [[Scouting Eye]], and [[Talking Corpse]]. Individual creatures with the coven ability also grant additional spells to any coven they join. A coven can also cast the [[Control Weather]] ritual, with a DC of 23 instead of the standard DC. <br>  <br> If a coven member's departure or death brings the coven below three members, the remaining members keep their elite adjustments for 24 hours, but without enough members to contribute the necessary actions, they can't cast coven spells."
  - name: "Snow Vision"
    desc: "Snow doesn't impair a winter hag's vision; she ignores [[Concealment]] from snowfall."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Curse of the Frozen Heart"
    desc: "**Saving Throw** DC 25 [[Will]] save <br>  <br> **Stage 1** 3d6 cold damage (1 day) <br>  <br> **Stage 2** the target has resistance 5 to cold (1 day) <br>  <br> **Stage 3** the target has resistance 10 to cold and treats no one as an ally (1 day) <br>  <br> **Stage 4** the target is immune to cold, treats no one as an ally, and is unfriendly to all creatures it wasn't hostile to (1 day) <br>  <br> **Stage 5** target becomes immune to cold and emotion effects, ceases to age, and is permanently dominated by the hag—if the hag is dead, the target remains at stage 4"
  - name: "Ice Climb"
    desc: "A winter hag can Climb at the listed Speed, but only on ice. She ignores difficult terrain from ice and snow, and she doesn't risk falling when crossing ice."
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +13, **Will** +16"
health:
  - name: HP
    desc: "145; **Immunities** cold, emotion; **Weaknesses** cold iron 5, fire 5"
abilities_mid:
  - name: "Thaw the Heart"
    desc: "If the hag observes a creature succeed at a Performance check with a result equal to or greater than 26, the hag becomes [[Slowed]] 1 and loses their immunity to emotion effects for 1 hour. <br>  <br> > [!danger] Effect: Thaw the Heart"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ice Staff +17 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+7 bludgeoning plus 1d6 cold"
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, unarmed), **Damage** 2d6+7 slashing plus 1d6 cold"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Ice Storm]], [[Rewrite Memory]]<br>**3rd** [[Enthrall]], [[Paralyze]]<br>**2nd** [[Environmental Endurance]] (At Will), [[See the Unseen]] (Constant)<br>**1st** [[Charm]], [[Frostbite]]"
  - name: "Coven Spells"
    desc: "DC 25, attack +17<br>**6th** [[Cursed Metamorphosis]]<br>**5th** [[Howling Blizzard]], [[Illusory Scene]], [[Scouting Eye]], [[Wall of Ice]]<br>**4th** [[Clairvoyance]], [[Rewrite Memory]], [[Talking Corpse]]<br>**3rd** [[Clairaudience]], [[Dream Message]]<br>**2nd** [[Augury]]<br>**1st** [[Charm]], [[Illusory Disguise]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The winter hag can take on the appearance of any Medium humanoid woman. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Kiss of Rime"
    desc: "`pf2:1` **Frequency** once per hour <br>  <br> **Effect** A shard of magic ice embeds itself within the flesh of a creature within 30 feet. The creature must save against the curse of the frozen heart."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Winter hags are as icy in demeanor as their name implies. Devoid of any trace of mortal warmth, they see emotion as a weakness and despise displays of it in any form. They demand the same from their wards and thralls, for despite their avowed uncaring nature, winter hags still seek out companionship, beckoning those left bitter by the world or drawn to stark and frigid beauty. Magical alterations and the occasional punishment soon turn these unfortunates into perfect vassals for the winter hag's court. Some brave souls, however, claim winter hags can be swayed to mercy by music.

A winter hag is flawless and cruel in appearance, a statuesque woman who looks as though they were carved from ice and pure white snow.

Hags are bizarre predators with uncertain origins, best known for targeting children and the young. To a one, they appear female, and they typically disguise themselves as mortal women in their day-to-day lives. Their powerful magic and manipulative tactics allow them to lure in the naive and vulnerable, exploiting their victims for their own sadistic purposes before kidnapping or devouring them. The typical hag is defined by a vain and controlling nature. Less malevolent hags may exist, but if so, they keep themselves well hidden to avoid the attentions of adventurers and their own abusive kin.

```statblock
creature: "Winter Hag"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
