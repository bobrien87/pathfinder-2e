---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mirror Seer"
level: "9"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16"
languages: "Common, Diabolic, Fey, Shadowtongue"
skills:
  - name: Skills
    desc: "Deception +21, Diplomacy +17, Occultism +19, Performance +17, Society +17, Stealth +17"
abilityMods: ["+2", "+2", "-1", "+4", "+3", "+5"]
abilities_top:
  - name: "Looking Glass Magic"
    desc: "The mirror seer accesses power from their wicked benefactor through two mirrors: one full-sized [[Malefic Mirror]] in their sanctum and an *enchanted hand mirror* they can carry on their person. <br>  <br> - **Malefic Mirror** The mirror seer must visit the *malefic mirror* once per day to retain their spellcasting abilities, and they can activate the mirror for special [[Scrying]] and [[Illusory Disguise]] spells as noted in the mirror's stat block. <br> - **Enchanted Hand Mirror** Without their *enchanted hand mirror* on their person, the mirror seer takes a –2 circumstance penalty to spell attack rolls and DCs and can't cast their 7th-rank spells. If it's not attended by the mirror seer, the hand mirror has AC 10, Hardness 0, and 1 HP."
armorclass:
  - name: AC
    desc: "27; **Fort** +14, **Ref** +17, **Will** +20"
health:
  - name: HP
    desc: "140"
abilities_mid:
  - name: "Rightfully Mine"
    desc: "`pf2:r` **Trigger** The mirror seer observes a creature making a Strike, casting a spell of 4th rank or lower, or using a special action (the triggering action must take 2 actions or fewer) <br>  <br> **Effect** The mirror seer expends a 4th-rank spell slot (or higher) to duplicate the triggering action. This mimicked action occurs immediately after the triggering action, using the triggering creature's statistics unless the mirror seer's are higher. The creature the mirror seer mimicked is then temporarily immune to this ability for 10 minutes."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +19 (`pf2:1`) (agile, magical, versatile s), **Damage** 1d4+8 piercing"
  - name: "Melee strike"
    desc: "Dagger +19 (`pf2:1`) (agile, magical, thrown 10, versatile s), **Damage** 1d4+8 piercing"
  - name: "Melee strike"
    desc: "Staff +19 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+8 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +18 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 29, attack +21<br>**6th** [[Scrying]]<br>**5th** (2 slots) [[Illusory Scene]], [[Shadow Blast]]<br>**4th** (3 slots) [[Clairvoyance]], [[Detect Scrying]], [[Peaceful Bubble]]<br>**3rd** (3 slots) [[Clairaudience]], [[Hypnotize]], [[Locate]]<br>**2nd** (3 slots) [[Invisibility]], [[Revealing Light]], [[Status]]<br>**1st** (3 slots) [[Alarm]], [[Daze]], [[Fear]], [[Figment]], [[Illusory Disguise (Self Only)]], [[Item Facade]], [[Prestidigitation]], [[Telekinetic Projectile]], [[Void Warp]]"
abilities_bot:
  - name: "A Fairer Face"
    desc: "`pf2:1` The mirror seer chooses a creature within 100 feet that can see its own reflection in a mirror. The creature must succeed at a DC 29 [[Will]] save or become [[Fascinated]] by their reflection for 1 minute. The creature can attempt a new save to end the effect at the end of each of its turns."
  - name: "Hall of Mirrors"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Effect** The mirror seer causes all surfaces in a @Template[type:burst|distance:30] within 100 feet to become reflective for 1 minute. Every creature in the area or that later enters the area must succeed at a DC 27 [[Will]] save or become [[Confused]] by the reflections and refractions. The confusion ends if the creature leaves the area, and the creature can attempt a new save to end the effect at the end of each of its turns. When the effect ends for a creature, that creature becomes temporarily immune for 10 minutes."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Seeking to be the most powerful and perfect creature in their domain, a mirror seer forges a deal with a nefarious entity for more power. Through a magic mirror called a *malefic mirror*, they communicate with this entity and spy on the events that unfold in their realm.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Mirror Seer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
